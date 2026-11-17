# Recherche : les briques pour transcrire et reformuler un brief vocal en streaming

Ticket : #3 (carte : #1). Date des relevés : 17 novembre 2026.

**Question.** Le **brief vocal** (voir `GLOSSARY.md`) suit ce parcours : le prospect dicte son besoin, la parole est transcrite en streaming et le texte s'affiche en direct. L'IA reformule ensuite ce texte en un brief structuré, envoyé par e-mail à Henri sous forme de **lead**. Quelles briques permettent ce parcours, et comment les assembler ? Les données de départ : un site en français, un volume faible (quelques briefs par semaine) et un hébergement probable sur Vercel.

> Chaque affirmation renvoie à sa source. Les prix sont ceux des pages officielles à la date ci-dessus. Les calculs de coût (« ≈ ») sont les miens. Les points non vérifiés à la source sont signalés **[à vérifier]**.

---

## 1. Synthèse

| Option STT | Streaming (texte en direct) | FR | Coût pour 3 min | Hébergement de l'audio | Entraînement sur les données |
|---|---|---|---|---|---|
| **Web Speech API** (navigateur) | Oui (`interimResults`) | Oui (selon le navigateur) | 0 € | Serveur du navigateur par défaut (Google pour Chrome), ou sur l'appareil avec `processLocally` | Aucun contrat avec vous |
| **Whisper dans le navigateur** (transformers.js + WebGPU) | Non natif (par segments) | Oui (modèles multilingues) | 0 € | Sur l'appareil | Aucun |
| **OpenAI** `gpt-live-transcribe` (temps réel) | Oui (WebSocket/WebRTC) | Oui | ≈ 0,05 $ | US par défaut ; EU possible (`eu.api.openai.com`, organisations éligibles) | Non par défaut |
| **OpenAI** `gpt-transcribe` (fichier, `stream=true`) | Après l'enregistrement seulement | Oui | ≈ 0,014 $ | Idem | Non par défaut |
| **Deepgram** Nova-3 multilingue / Flux multi | Oui (WebSocket) | Oui (`fr`) | ≈ 0,017 à 0,023 $ | EU possible (`api.eu.deepgram.com`, GA) | Programme d'amélioration actif sauf `mip_opt_out=true` |
| **AssemblyAI** streaming | Oui (WebSocket) | Oui (32 langues, dont `fr`) | ≈ 0,008 à 0,015 $ | EU possible (`streaming.eu.assemblyai.com`, même prix) | Partage actif sauf opt-out (impossible en gratuit) |
| **Mistral Voxtral Realtime** | Oui (WebSocket) | Oui (13 langues) | ≈ 0,018 à 0,024 $ | Endpoint global sans engagement de lieu ; endpoint EU sans garantie pour l'audio **[à vérifier]** | Non par défaut (payant) **[à vérifier]** |

Le coût d'une reformulation par Claude se compte en centimes : ≈ 0,04 $ avec Opus 5.5, une fraction de centime avec Haiku 5.5. Avec quelques briefs par semaine, **la facture totale reste sous 1 $ par mois** quelle que soit l'option, et les crédits gratuits (Deepgram 200 $, AssemblyAI 50 $) couvrent des années d'usage. Le coût ne départage donc pas les options. Ce qui les départage : l'expérience de streaming, la couverture des navigateurs et le RGPD.

**Recommandation : l'architecture B** (§ 3). Le navigateur se connecte directement à un STT temps réel hébergé dans l'UE (Deepgram EU par défaut), avec un jeton éphémère. Une fonction Vercel appelle ensuite Claude pour la reformulation, puis Resend (région UE) pour l'envoi.

---

## 2. Les briques, une par une

### 2.1 Transcription dans le navigateur

**Web Speech API (`SpeechRecognition`)**
- Le navigateur décide où se fait la reconnaissance : « Depending on the browser, your audio might be sent to a server-based recognition service […] or it might be processed on the user's device ». Sur certains navigateurs, un moteur serveur est utilisé par défaut, sauf si l'on exige `processLocally = true` ([MDN, Using the Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API) ; [MDN, SpeechRecognition](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition)). Dans Chrome, ce serveur est celui de Google : c'est un fait connu, mais MDN ne le dit pas noir sur blanc **[à vérifier]**.
- Mode sur l'appareil : `SpeechRecognition.available()` et `install()` téléchargent un pack de langue (~60 Mo par langue sur desktop selon l'équipe Chromium). Ce mode est disponible depuis Chrome 139 ([Intent to Ship : On-device Web Speech API](https://groups.google.com/a/chromium.org/g/blink-dev/c/VNOok2dbmHM) ; [fil chrome-ai-dev-preview](https://groups.google.com/a/chromium.org/g/chrome-ai-dev-preview-discuss/c/Rlyc2uAsFCY)). Rien ne confirme que le pack français existe **[à vérifier]**.
- Les résultats intermédiaires (`interimResults`) donnent l'affichage en direct.
- Support : la fonctionnalité n'est pas « Baseline » (« does not work in some of the most widely-used browsers », [MDN](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition)). En pratique, les navigateurs Chromium et Safari l'ont (avec préfixe `webkit`), Firefox non **[à vérifier sur la table de compatibilité MDN]**.
- RGPD : en mode serveur, l'audio part chez l'éditeur du navigateur. Aucun contrat (DPA) ne vous lie à lui, vous ne maîtrisez ni le lieu ni la conservation, et c'est difficile à documenter dans une politique de confidentialité.

**Whisper dans le navigateur (transformers.js, WebGPU)**
- `pipeline("automatic-speech-recognition", "onnx-community/whisper-…", { device: "webgpu" })` ([Hugging Face, Running models on WebGPU](https://huggingface.co/docs/transformers.js/guides/webgpu)).
- WebGPU couvre environ 85 % des navigateurs en mars 2026. Le support Firefox et Safari est partiel (même source).
- Whisper travaille par segments d'audio. Le streaming n'est pas natif : il faut découper l'audio, et le texte arrive avec un retard de quelques secondes. Le modèle multilingue fait des dizaines à des centaines de Mo à télécharger, ce qui pèse sur mobile (ordre de grandeur, **[à mesurer]**).
- RGPD : idéal, puisque l'audio ne quitte jamais l'appareil.

### 2.2 Transcription par API

**OpenAI**
- Modèles actuels : `gpt-transcribe` (fichier, `stream=true`) et `gpt-live-transcribe` (temps réel). `whisper-1`, `gpt-4o-transcribe` et `gpt-4o-mini-transcribe` sont dépréciés, avec un arrêt prévu le 26 février 2027. Fichiers jusqu'à 25 Mo ([Speech to text](https://developers.openai.com/api/docs/guides/speech-to-text)).
- Temps réel : WebSocket `wss://api.openai.com/v1/realtime?intent=transcription`, deltas `conversation.item.input_audio_transcription.delta`, paramètre `languages: ["fr"]`. `gpt-live-transcribe` ne gère pas le VAD serveur : il faut un VAD côté client ([Realtime transcription](https://developers.openai.com/api/docs/guides/realtime-transcription)). Côté navigateur, la doc décrit WebRTC avec une clé éphémère (`POST /v1/realtime/client_secrets`) ([Realtime WebRTC](https://developers.openai.com/api/docs/guides/realtime-webrtc)). Rien ne confirme ce parcours pour une session de transcription seule **[à vérifier]**.
- Prix : `gpt-transcribe` 0,0045 $/min, `gpt-live-transcribe` 0,017 $/min ([Pricing](https://developers.openai.com/api/docs/pricing)). Pour 3 min : ≈ 0,014 $ ou ≈ 0,05 $.
- Données : pas d'entraînement par défaut. `/v1/audio/transcriptions` ne garde rien pour la surveillance des abus, `/v1/realtime` garde 30 jours. Les deux sont éligibles au ZDR ([Your data](https://developers.openai.com/api/docs/guides/your-data)). Une résidence UE existe (`eu.api.openai.com`, stockage et traitement régionaux, modèles `gpt-transcribe` et `gpt-live-transcribe` inclus), mais elle est réservée aux « eligible organizations », se choisit à la création du projet et coûte 10 % de plus sur les modèles récents ([Data residency](https://developers.openai.com/api/docs/guides/data-residency)). L'éligibilité d'un petit compte est incertaine **[à vérifier]**.

**Deepgram**
- Le français (`fr`) est pris en charge par Nova-3 (monolingue et multilingue) et par Flux via `flux-general-multi` ([Models & languages](https://developers.deepgram.com/docs/models-languages-overview)).
- Prix en paiement à l'usage, en streaming : Nova-3 monolingue 0,0048 $/min, multilingue 0,0058 $/min ; Flux multilingue 0,0078 $/min (tarif « promo ») ; 200 $ de crédit offert ([Pricing](https://deepgram.com/pricing)). Pour 3 min : ≈ 0,015 à 0,023 $.
- Navigateur : `POST /v1/auth/grant` renvoie un JWT valable 30 s par défaut (3600 s max). Il suffit qu'il soit valide à l'ouverture du WebSocket `/v1/listen` ([Token-based auth](https://developers.deepgram.com/guides/fundamentals/token-based-authentication)).
- UE : l'endpoint `api.eu.deepgram.com` est en GA, avec un traitement dans des régions AWS de l'UE ([annonce Deepgram](https://deepgram.com/learn/deepgram-eu-endpoint-now-generally-available) ; [Regional endpoints](https://developers.deepgram.com/reference/regional-endpoints)).
- Entraînement : le programme d'amélioration des modèles (MIP) s'applique sauf si l'on ajoute `mip_opt_out=true` à chaque requête. Les données exclues ne sont gardées que le temps du traitement ([MIP](https://developers.deepgram.com/docs/the-deepgram-model-improvement-partnership-program)). Depuis mars 2026, l'opt-out ne change pas le prix en paiement à l'usage ([changelog](https://developers.deepgram.com/changelog/2026/3/5)) **[à reconfirmer]**.

**AssemblyAI**
- Streaming : Universal-Streaming à 0,15 $/h, remplacé par AssemblyAI-STT-3.7-Realtime à 0,30 $/h, facturé à la durée de session. 50 $ de crédit offert, limite de 5 flux par minute en gratuit ([Pricing](https://www.assemblyai.com/pricing)). Pour 3 min : ≈ 0,008 à 0,015 $.
- Langues : « All streaming models code-switch across 32 languages », dont `fr` ([Multilingual streaming](https://www.assemblyai.com/docs/universal-streaming/multilingual-transcription)).
- UE : `streaming.eu.assemblyai.com`, « EU region is the same price as US » ([Pricing](https://www.assemblyai.com/pricing)).
- Navigateur : jeton temporaire émis par le serveur ([Temporary token](https://www.assemblyai.com/docs/universal-streaming/authenticate-with-a-temporary-token)).
- Entraînement : partage pour l'amélioration des modèles, avec opt-out dans le tableau de bord pour les comptes payants seulement. Les comptes gratuits ne peuvent pas s'en exclure ([FAQ opt-out](https://www.assemblyai.com/docs/faq/how-to-opt-out-of-data-sharing-for-our-model-improvement-program)).

**Mistral Voxtral**
- Voxtral Realtime : latence réglable jusqu'à moins de 200 ms, 13 langues dont le français, 0,006 $/min, poids ouverts sous Apache 2.0. Voxtral Mini Transcribe V2 (lot) : 0,003 $/min ([annonce Voxtral Transcribe 2](https://mistral.ai/news/voxtral-transcribe-2)). Le successeur `voxtral-mini-transcribe-realtime-3` est en Public Preview, à environ 0,008 $/min, avec une latence de 80 à 2 400 ms ([fiche modèle](https://docs.mistral.ai/models/voxtral-mini-transcribe-realtime-3-0.md)).
- WebSocket `wss://api.mistral.ai/v1/audio/transcriptions/realtime`. Pour le navigateur, le serveur émet un jeton `rt_*` ([Realtime transcription](https://docs.mistral.ai/studio/audio/speech-to-text/transcribe-in-realtime) ; [Client auth](https://docs.mistral.ai/studio/audio/speech_to_text/realtime_transcription/client_auth)).
- Lieu : l'endpoint global « does not commit to a specific inference location ». `api.eu.mistral.ai` traite dans l'UE et l'AELE (+10 %), mais ne sert que les modèles hébergés dans la région. La doc ne mentionne pas l'audio ([Regional inference](https://docs.mistral.ai/inference/regional-inference)) **[à vérifier : Voxtral Realtime sur l'endpoint EU]**.
- Entraînement : en mode gratuit, Mistral « may use your data ». En paiement à l'usage, l'opt-out est possible ([Help center](https://help.mistral.ai/en/articles/347617-do-you-use-my-user-data-to-train-your-artificial-intelligence-models)). Le réglage par défaut et la conservation (30 jours selon des sources secondaires) restent **[à vérifier dans le DPA]**.

### 2.3 Reformulation : Claude

- Modèle par défaut : `claude-opus-5-5`, à 4 $ / 20 $ par million de tokens en entrée / sortie. Alternative économique : `claude-haiku-5-5`, à 0,10 $ / 0,50 $ (référence du skill `claude-api`, prix relevés le 3 novembre 2026 ; [Pricing](https://platform.claude.com/docs/en/about-claude/pricing)).
- Coût : 3 min de parole en français font environ 450 mots, soit ~1k tokens. Avec un prompt système, on arrive à ~2k tokens en entrée et ~1,5k en sortie (réflexion comprise). Cela donne ≈ 0,04 $ avec Opus 5.5 et ≈ 0,001 $ avec Haiku 5.5. Avec Opus 5.5, l'effort par défaut est `medium` et la réflexion ne peut pas être désactivée. Une reformulation est une tâche simple : `effort: "low"` suffit. Les sorties structurées (`output_config.format`, schéma JSON du brief) garantissent le format.
- Streaming : `messages.stream()` dans une fonction Vercel. Le prospect voit le brief se rédiger pendant que la réponse est relayée en flux.
- Données : les prompts et les sorties ne sont pas conservés par défaut, sauf pour les « Covered Models » (Fable, Mythos), qui imposent 30 jours. Rien n'est utilisé pour l'entraînement sans permission expresse. Une conservation jusqu'à 2 ans reste possible si un contenu est signalé par les systèmes de sécurité ([API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)).
- Lieu : `inference_geo` n'accepte que `"global"` ou `"us"`, et le « workspace geo » n'existe qu'en `"us"`. **Il n'y a pas d'option UE** ([Data residency](https://platform.claude.com/docs/en/manage-claude/data-residency)). Le texte du brief part donc hors UE, avec Anthropic comme sous-traitant (transfert à encadrer par le DPA d'Anthropic : clauses contractuelles types et/ou Data Privacy Framework **[à vérifier dans le DPA]**). Seul le texte transcrit est envoyé à Claude, jamais l'audio.

### 2.4 Envoi de l'e-mail : Resend

- Offre gratuite : 3 000 e-mails par mois, plafonnés à 100 par jour ([Pricing](https://resend.com/pricing)). C'est largement suffisant.
- Les régions d'envoi incluent `eu-west-1` (Irlande). En revanche, « all account data is stored in the United States » ([Regions](https://resend.com/docs/dashboard/domains/regions)). Le contenu du lead transite donc par un sous-traitant américain. Alternative : un SMTP européen (Brevo, Scaleway TEM…) **[non étudié ici]**.

### 2.5 Hébergement : Vercel

- Fonctions (Fluid compute) : durée max de 300 s en Hobby et de 800 s en Pro (1 800 s en bêta). La limite inclut le temps de streaming de la réponse. Corps de requête limité à 4,5 Mo, sans limite pour les réponses streamées. Région unique par défaut (`iad1`), modifiable ([Functions limits](https://vercel.com/docs/functions/limitations)). Une région Paris (`cdg1`) existe **[à vérifier dans la liste des régions]**.
- Les WebSockets sont en **bêta publique** depuis le 22 juin 2026, sur tous les plans. Une connexion est fermée à la durée max de la fonction (300 s en Hobby). Il faut `experimental_upgradeWebSocket()` avec Next.js. La mémoire est facturée tant que la connexion reste ouverte ([KB WebSocket](https://vercel.com/kb/guide/do-vercel-serverless-functions-support-websocket-connections)).
- Conséquence : relayer l'audio par Vercel est possible, mais inutile et fragile (bêta, plafond de 5 min en Hobby pour un brief de 2 à 3 min). **Mieux vaut que le navigateur se connecte directement au STT avec un jeton éphémère**, et que Vercel ne serve qu'à émettre le jeton (requête courte) et à streamer la réponse de Claude (bien sous 300 s).

---

## 3. Architectures candidates

### A. Tout dans le navigateur avec la Web Speech API, puis Claude

```
Micro → SpeechRecognition (interimResults, lang=fr-FR) → texte en direct
      → POST /api/brief (Vercel) → Claude (stream) → aperçu du brief → Resend → Henri
```
- **Pour** : aucun compte STT, rien à payer pour la transcription, le moins de code possible, et un texte en direct natif.
- **Contre** : pas de Firefox, un comportement et une qualité qui varient selon le navigateur et sans contrôle de votre part, et des coupures sur les silences longs (à relancer). Le point le plus lourd : **dans Chrome, l'audio part par défaut chez Google, hors de tout contrat**, ce qui est difficile à justifier au regard du RGPD. `processLocally` corrige ce point, mais au prix d'un pack de ~60 Mo, de Chrome 139 ou plus, et d'un pack français non confirmé.
- **Usage** : en repli, ou en prototype rapide.

### B. Un STT temps réel dans l'UE, en connexion directe depuis le navigateur (recommandée)

```
1. GET /api/stt-token (Vercel)  → jeton éphémère (Deepgram /v1/auth/grant, TTL court)
2. Micro → WebSocket direct wss://api.eu.deepgram.com/v1/listen?model=nova-3&language=fr&mip_opt_out=true
         → texte en direct (résultats intermédiaires et finaux)
3. Le prospect relit et corrige le texte, puis valide
4. POST /api/brief (Vercel) → Claude claude-opus-5-5 (effort low, sortie structurée, stream) → aperçu
5. Resend (eu-west-1) → e-mail « Lead : brief vocal » à Henri (+ accusé de réception au prospect)
```
- **Pour** : une latence faible et un vrai streaming, sur tous les navigateurs modernes (seuls `getUserMedia` et WebSocket sont requis). L'audio est traité dans l'UE sans servir à l'entraînement. Aucun WebSocket ne passe par Vercel. Le coût est d'environ 0,06 $ par brief, couvert par les crédits gratuits.
- **Contre** : un compte et un DPA de plus. Il faut penser à `mip_opt_out=true` à chaque connexion. Le texte (pas l'audio) part chez Anthropic aux États-Unis.
- **Variantes du STT** (même schéma) :
  - **AssemblyAI EU** : le moins cher et au même prix qu'aux États-Unis, mais l'opt-out d'entraînement n'existe qu'en compte payant.
  - **Mistral Voxtral Realtime** : un acteur français, mais le traitement dans l'UE n'est pas garanti pour l'audio sur l'endpoint EU, et la v3 est en preview.
  - **OpenAI `gpt-live-transcribe`** : la résidence UE est réservée aux organisations éligibles, et c'est l'option la plus chère (0,017 $/min).

### C. Transcription locale (Whisper dans le navigateur), puis Claude

```
Micro → AudioWorklet (segments de ~5 s) → Whisper (transformers.js, WebGPU) → texte quasi direct
      → POST /api/brief → Claude → Resend
```
- **Pour** : l'audio ne quitte jamais l'appareil, ce qui donne le meilleur argument RGPD et un message fort (« votre voix reste chez vous »). Aucun coût de transcription.
- **Contre** : un modèle lourd à télécharger, environ 15 % de navigateurs sans WebGPU, des mobiles lents. Le texte arrive par blocs avec quelques secondes de retard : ce n'est pas du vrai streaming. Le découpage et le recollage des segments demandent un vrai travail d'ingénierie. Le texte part tout de même chez Anthropic.
- **Usage** : seulement si l'argument « rien ne sort de votre navigateur » devient central dans le positionnement.

### Recommandation

**B avec Deepgram EU**, parce que :
- c'est la seule option qui combine un vrai streaming, tous les navigateurs, un traitement dans l'UE en GA et une exclusion de l'entraînement documentée à la requête ;
- le coût est négligeable ;
- Vercel ne porte aucune connexion longue.

Deux ajouts à prévoir :
- un **repli texte** (zone de saisie) quand le micro est refusé ou indisponible ;
- une **étape de relecture** du texte transcrit avant l'envoi, qui améliore la qualité du lead et matérialise le consentement.

Garder Voxtral en option « souveraine » si Mistral confirme le traitement de Voxtral Realtime dans l'UE.

---

## 4. Conséquences RGPD (pour le ticket « Légal » de la carte)

- **Nature de la donnée** : la voix est une donnée personnelle. Elle ne devient une donnée biométrique (art. 9) que si elle sert à identifier une personne, ce qui n'est pas le cas ici. Le contenu du brief peut aussi contenir des données personnelles (nom, entreprise, coordonnées).
- **Minimisation** : ne jamais stocker l'audio. Il n'est que streamé vers le STT puis oublié. Seuls le texte et le brief sont conservés, dans l'e-mail du lead.
- **Information et consentement** : avant d'ouvrir le micro, une mention claire et une action positive (bouton « Commencer la dictée » accompagné d'un texte qui nomme les sous-traitants et le transfert hors UE). Base légale : mesures précontractuelles à la demande du prospect (art. 6.1.b) ou consentement **[à trancher dans le ticket Légal]**.
- **Sous-traitants à lister et à couvrir par un DPA** : le STT (Deepgram, UE), Anthropic (États-Unis, transfert à encadrer), Resend (données de compte aux États-Unis) et Vercel.
- **Durée de conservation** : la durée de vie du lead dans la boîte d'Henri (par exemple 3 ans sans suite, selon les recommandations CNIL sur la prospection) **[à fixer]**.

---

## 5. Incertitudes restantes

1. La qualité réelle en français de chaque STT sur un brief métier (jargon technique, noms propres). Elle n'a pas été mesurée : un test de 3 à 4 enregistrements identiques sur Deepgram, AssemblyAI et Voxtral trancherait.
2. Voxtral Realtime est-il servi par `api.eu.mistral.ai` ? Quelles sont la conservation et l'exclusion de l'entraînement par défaut en paiement à l'usage ?
3. L'éligibilité d'un petit compte à la résidence UE d'OpenAI.
4. Le pack français de la Web Speech API sur l'appareil, et la table de compatibilité exacte des navigateurs.
5. Le fait qu'Anthropic n'ait pas d'inférence dans l'UE est documenté. Le mécanisme de transfert reste à lire dans le DPA.
