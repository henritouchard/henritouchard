# Recherche : Voxtral Realtime et Mistral pour la dictée et la reformulation du brief

Ticket : #11 (carte : #1). Date des relevés : 18 novembre 2026.

**Question.** Mistral remplace Deepgram (dictée) et Claude (reformulation) (voir #9). Quatre points à trancher :
1. le navigateur peut-il se connecter directement à Voxtral Realtime avec un jeton éphémère, ou faut-il relayer l'audio par le serveur (Astro Node sur le VPS) ? Avec quel protocole et quel format audio ?
2. où les données sont-elles traitées, combien de temps Mistral les garde, existe-t-il un DPA ?
3. quelle qualité et quelle latence en français ?
4. quel modèle pour la reformulation, et à quel coût par brief ?

La recherche précédente (branche `research/brief-vocal`, `docs/research/brief-vocal.md`) couvrait déjà Voxtral à grands traits. Ce document approfondit seulement Mistral.

> Chaque affirmation renvoie à sa source. Les prix sont ceux des pages officielles à la date ci-dessus. Les calculs de coût (« ≈ ») sont les miens. Les points non vérifiés à la source sont signalés **[à vérifier]**.

---

## 1. Synthèse

| Point | Réponse courte |
|---|---|
| Modèle de dictée | `voxtral-mini-transcribe-realtime-3` (Voxtral 3, sorti le 20 octobre 2026, **Public Preview**), 0,008 $/min |
| Connexion | **Directe depuis le navigateur** : le serveur émet un jeton `rt_*` (`POST /v1/client/sessions`), le navigateur ouvre le WebSocket avec ce jeton en sous-protocole. Aucun relais audio nécessaire |
| Protocole et format | WebSocket `wss://api.mistral.ai/v1/audio/transcriptions/realtime?model=…`, messages JSON ; audio PCM 16 bits little-endian mono (`pcm_s16le`), 16 kHz par défaut, encodé en base64 dans `input_audio.append` |
| Latence | Réglable de 80 à 1 200 ms (ou 2 400 ms) ; 480 ms recommandé. Les deltas de texte sont définitifs (jamais corrigés) |
| Français | Pris en charge. Sur FLEURS, Voxtral Realtime (génération 2602) : 6,4 % de WER à 480 ms, 5,2 % à 2,4 s, contre 4,3 % hors ligne. Pas de chiffre français publié pour la v3 |
| Lieu de traitement | Données « hébergées dans l'UE par défaut », mais l'endpoint global ne garantit pas le lieu d'inférence. L'endpoint `api.eu.mistral.ai` le garantit (+10 %), sans confirmation pour le WebSocket temps réel **[à vérifier]** |
| Conservation | 30 jours glissants (surveillance des abus) par défaut ; ZDR sur demande, à la discrétion de Mistral |
| Entraînement | Par défaut en mode gratuit ; opt-out dans l'Admin (Privacy) en paiement à l'usage |
| DPA | Oui, intégré automatiquement aux conditions (version du 27 juillet 2026), CCT 2021/914 pour les transferts |
| Reformulation | `mistral-small-2603` (Mistral Small 4) : ≈ 0,0005 $ par brief |
| Coût total par brief | ≈ 0,017 $ (dictée 0,016 $ + reformulation 0,0005 $) |

**Recommandation : connexion directe du navigateur** avec un jeton `rt_*` éphémère, Mistral Small 4 pour la reformulation, compte payant avec l'opt-out d'entraînement activé, et un test de l'endpoint EU avant la mise en production (§ 5).

---

## 2. Voxtral Realtime : API, connexion et format

### 2.1 Les modèles

- **Voxtral 3** est sorti le 20 octobre 2026. Il comprend un modèle temps réel, `voxtral-mini-transcribe-realtime-3-0` (alias `voxtral-mini-transcribe-realtime-3` et `…-latest`) ([changelog](https://docs.mistral.ai/resources/changelogs) ; [fiche modèle](https://docs.mistral.ai/models/voxtral-mini-transcribe-realtime-3-0)).
- Statut : **Public Preview**, 0,008 $/min d'audio en entrée, latence réglable de 80 à 2 400 ms. Diarisation, détection de fin de tour et biais de contexte sont intégrés ([fiche modèle](https://docs.mistral.ai/models/voxtral-mini-transcribe-realtime-3-0) ; [pricing](https://docs.mistral.ai/inference/pricing)).
- Le modèle précédent, `voxtral-mini-transcribe-realtime-2602` (février 2026, 0,006 $/min, poids ouverts Apache 2.0), est remplacé par la v3 ([annonce Voxtral Transcribe 2](https://mistral.ai/news/voxtral-transcribe-2) ; [migration](https://docs.mistral.ai/studio/audio/migrate-from-voxtral-2)). Sa date de retrait n'est pas publiée (section vide) **[à vérifier]**.
- L'API temps réel est publique, en paiement à l'usage, avec une clé d'API standard.

### 2.2 Connexion directe du navigateur : oui

- Le serveur appelle `POST /v1/client/sessions` avec la clé d'API, en envoyant `purpose: "realtime"` et `model`. La réponse (201) contient `client_secret.value` (jeton préfixé `rt_`) et `expires_at`. La clé d'API doit avoir la permission `create_client_session` ([API Realtime Sessions](https://docs.mistral.ai/api/endpoint/realtime/sessions)).
- Le jeton expire après « approximately 900 seconds ». Il est lié à un modèle (« A token minted for model A is rejected if used with model B ») et **réutilisable jusqu'à expiration** ([Client authentication](https://docs.mistral.ai/studio/audio/speech_to_text/realtime_transcription/client_auth)).
- Le navigateur le passe en sous-protocole WebSocket, car il ne peut pas poser d'en-tête `Authorization` : « this header is the only supported transport for `rt_*` tokens ».

  ```js
  const ws = new WebSocket(
    `wss://api.mistral.ai/v1/audio/transcriptions/realtime?model=${model}`,
    ["realtime", token] // Sec-WebSocket-Protocol
  );
  ```

- **Mise en garde** : la page « Client authentication » est classée dans la section « Deprecated » de la documentation (celle de Voxtral 2), et son exemple utilise encore le modèle 2602. La page actuelle sur le temps réel ne parle que de la clé d'API en en-tête `Authorization`. En revanche, l'endpoint `POST /v1/client/sessions` figure toujours dans la référence d'API, hors de la section dépréciée ([Realtime transcription](https://docs.mistral.ai/studio/audio/speech-to-text/transcribe-in-realtime) ; [API Realtime Sessions](https://docs.mistral.ai/api/endpoint/realtime/sessions)). Que le jeton `rt_*` fonctionne avec `voxtral-mini-transcribe-realtime-3` est donc probable, mais **[à vérifier par un test]**.
- Conséquence pratique : le serveur Astro n'a qu'une route courte (`POST /api/dictee/jeton`) qui émet le jeton juste avant la connexion (la doc conseille de ne pas l'émettre au chargement de la page). Aucun WebSocket ne passe par le VPS.
- Risque : un jeton volé permet ~15 min de transcription aux frais d'Henri, soit au plus ≈ 0,12 $. Il suffit de limiter le débit de la route du jeton (par IP) et, si besoin, de la protéger par un anti-robot.

**Repli : relais par le serveur.** Il n'est utile que si le jeton `rt_*` ne fonctionne pas avec la v3, ou si l'endpoint EU n'accepte pas les jetons client. Le relais est faisable sur le VPS (Node gère les WebSockets, Caddy les proxifie sans configuration particulière), mais il ajoute du code, un saut réseau et une connexion longue à surveiller. Il ne change rien au lieu de traitement chez Mistral.

### 2.3 Protocole et format audio

Source : [Realtime transcription](https://docs.mistral.ai/studio/audio/speech-to-text/transcribe-in-realtime).

- **Messages client** : `session.update` (réglages), `input_audio.append` (audio en base64 dans le champ `audio`, un message par bloc), `input_audio.end`.
- **Événements serveur** : `session.created`, `session.updated`, `transcription.text.delta` (texte au fil de l'eau), `transcription.done` (texte complet après `input_audio.end`), `error`. Avec la diarisation : `transcription.segment`. Avec la détection de tours : `turn.start`, `turn.eager_end`, `turn.resume`, `turn.end`.
- **Format** : `pcm_s16le` (PCM 16 bits signé little-endian), mono, 16 000 Hz par défaut, réglable via `audio_format`. Aucun codec compressé (Opus…) n'est mentionné. Côté navigateur, il faut donc un `AudioWorklet` qui convertit le Float32 du micro en Int16 à 16 kHz, puis l'encode en base64.
- **Réglages verrouillés** : « Session fields cannot be changed after audio has started ». Il faut tout envoyer dans le premier `session.update` (`language: "fr"`, `target_streaming_delay_ms`).
- **Limites** : l'audio et le `context_bias` partagent une fenêtre de 65 536 tokens. Au-delà, erreur 400, sans troncature ([Limits](https://docs.mistral.ai/studio/audio/specs-and-limits/limits)). Aucune durée maximale de session n'est publiée **[à vérifier]**. Une dictée de 2 min devrait tenir largement, mais le rapport secondes d'audio / tokens n'est pas documenté **[à vérifier]**.

### 2.4 Latence des résultats

- `target_streaming_delay_ms` : tout entier de 80 à 1 200, ou 2 400. Plus court, c'est plus rapide mais moins précis ([Limits](https://docs.mistral.ai/studio/audio/specs-and-limits/limits) ; [Latency](https://docs.mistral.ai/studio/audio/concepts/latency)). Point de départ recommandé : **480 ms**.
- Il n'y a pas de résultat « partiel » puis « final » : chaque delta « is final when you receive it » et ne corrige jamais le texte précédent. L'affichage est donc simple (on ajoute le texte au textarea), mais une erreur reste à l'écran jusqu'à ce que le prospect la corrige.
- Voxtral 3 annonce une transcription de qualité « at sub-500ms latency » ([annonce Voxtral 3](https://mistral.ai/news/voxtral-3/)). La latence réseau s'y ajoute (deux trajets) : la doc conseille de la mesurer depuis l'endroit où sont les utilisateurs.

---

## 3. Qualité en français

- Le français fait partie des 13 langues de Voxtral Realtime 2602 ([annonce Voxtral Transcribe 2](https://mistral.ai/news/voxtral-transcribe-2)). La v3 annonce 45 langues et dialectes en temps réel, sans les nommer ; le français figure dans la liste des modèles par fichier ([Languages](https://docs.mistral.ai/studio/audio/specs-and-limits/languages)). La prise en charge du français par la v3 temps réel est quasi certaine, mais pas écrite **[à vérifier]**.
- **Chiffres publiés (génération 2602, FLEURS, français)** ([fiche Hugging Face](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)) :

  | Modèle | Délai | WER français |
  |---|---|---|
  | Voxtral Mini Transcribe 2 (fichier) | hors ligne | 4,32 % |
  | Voxtral Realtime 2602 | 2 400 ms | 5,23 % |
  | Voxtral Realtime 2602 | 960 ms | 5,68 % |
  | Voxtral Realtime 2602 | 480 ms | 6,42 % |
  | Voxtral Realtime 2602 | 240 ms | 8,00 % |
  | Voxtral Realtime 2602 | 160 ms | 9,75 % |

- Pour la v3, Mistral ne publie que des moyennes multilingues en graphique, et affirme des résultats « state-of-the-art » en français pour le modèle Small (par fichier, pas le temps réel) ([annonce Voxtral 3](https://mistral.ai/news/voxtral-3/)). Aucun chiffre français pour `voxtral-mini-transcribe-realtime-3` **[non publié]**.
- FLEURS est de la lecture à voix haute. Une dictée spontanée (hésitations, jargon métier, noms propres) donnera un WER plus élevé. Le `context_bias` (vocabulaire métier) peut aider, mais il est annoncé « optimized for English », les autres langues étant « experimental » ([annonce Voxtral Transcribe 2](https://mistral.ai/news/voxtral-transcribe-2)).
- Je n'ai trouvé aucun retour indépendant fiable (benchmark tiers) sur le français en temps réel **[non confirmé]**.
- Lecture : à 480 ms, environ 1 mot sur 16 est faux sur de la parole lue. C'est suffisant pour un brief que le prospect relit, et la reformulation lisse le reste. Pour gagner en précision sans gêner la dictée, 960 ms est un bon compromis (le texte arrive avec ~1 s de retard).

---

## 4. Données, RGPD et DPA

### 4.1 Lieu de traitement

- Help center : « By default, your data is hosted in the European Union », sauf si l'on choisit l'endpoint US. Selon la fonctionnalité, les données peuvent être « temporarily processed outside the EU », chez les sous-traitants listés dans le Trust Center ([Where do you store my data?](https://help.mistral.ai/en/articles/347629-where-do-you-store-my-data-or-my-organization-s-data)).
- Doc d'inférence régionale : pour l'endpoint global `api.mistral.ai`, « Mistral does not commit to a specific inference location ». L'endpoint `api.eu.mistral.ai` traite dans « multiple data centers in EU and EFTA countries », facturé 1,1× le prix de liste. Il ne sert que les modèles hébergés dans la région (à lister via `models.list`), et la garantie tombe si l'on utilise une fonctionnalité non prise en charge ([Regional inference](https://docs.mistral.ai/inference/regional-inference)).
- Voxtral 3 est « hosted through our European, US, and global endpoints » ([annonce Voxtral 3](https://mistral.ai/news/voxtral-3/)). Mais aucune page ne documente `wss://api.eu.mistral.ai/v1/audio/transcriptions/realtime`, ni l'émission de jetons `rt_*` sur l'endpoint EU **[à vérifier par un test]**. La surcharge de 10 % est décrite pour les tokens ; son application à l'audio à la minute n'est pas précisée **[à vérifier]**.
- Les données de compte (clés, facturation, statistiques) peuvent être traitées hors région, même avec l'endpoint EU ([Regional inference](https://docs.mistral.ai/inference/regional-inference)).

### 4.2 Conservation

- Par défaut, sur l'API : les entrées et sorties sont gardées le temps de générer la réponse, puis **30 jours glissants** pour la surveillance des abus ([Privacy Policy](https://legal.mistral.ai/terms/privacy-policy/), page non lisible par mon outil, chiffre repris de sa citation dans les résultats de recherche **[à relire sur la page]**). Elles peuvent être gardées plus longtemps en cas de violation de la politique d'usage ou d'obligation légale.
- **Zero Data Retention (ZDR)** : seulement en compte payant et pour les appels sans état. Il faut le demander au support en justifiant un « legitimate reason » ; Mistral accepte ou refuse « at its discretion ». Les endpoints couverts incluent `/v1/chat/completions` et `/v1/audio/transcriptions`, mais **le WebSocket temps réel n'est pas cité** ([Zero data retention](https://docs.mistral.ai/admin/monitor-comply/zero-data-retention) ; [Help center ZDR](https://help.mistral.ai/en/articles/347612-can-i-activate-zero-data-retention-zdr)) **[à vérifier : couverture de `/v1/audio/transcriptions/realtime`]**.

### 4.3 Entraînement

- En mode gratuit, Mistral « may use your data (input and output) » pour entraîner ses modèles. En paiement à l'usage, le client peut s'en exclure à tout moment, via l'Admin, menu Privacy ([Do you use my data to train?](https://help.mistral.ai/en/articles/347617-do-you-use-my-user-data-to-train-your-artificial-intelligence-models) ; [Opt-out](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training)). Le réglage par défaut en paiement à l'usage n'est pas écrit **[à vérifier : activer l'opt-out explicitement]**.
- Le DPA confirme : Mistral, en tant que responsable de traitement, peut entraîner ses modèles « unless Customer is or has opted-out of training » ([DPA, § 2.3](https://legal.mistral.ai/terms/data-processing-addendum/)).

### 4.4 DPA et sous-traitants

- Le **Data Processing Addendum** (en vigueur au 27 juillet 2026) « is incorporated in the Agreement by reference » : il s'applique sans signature séparée ([DPA](https://legal.mistral.ai/terms/data-processing-addendum/)).
- Il réserve à Mistral un rôle de responsable de traitement pour la surveillance automatisée des abus et l'entraînement (sauf opt-out). Cette réserve tombe avec le ZDR (§ 2.3).
- Transferts : vers les pays adéquats, ou via les CCT (décision 2021/914). Le Data Privacy Framework n'est pas cité (§ 8).
- Sous-traitants : liste tenue à jour sur [trust.mistral.ai/subprocessors](https://trust.mistral.ai/subprocessors), avec abonnement par e-mail aux changements et droit d'objection sous 10 jours (§ 7). La page est rendue en JavaScript et je n'ai pas pu la lire : **noms et lieux des sous-traitants [non confirmés]**.
- Indice secondaire : Open Terms Archive a relevé en février 2025 l'ajout des États-Unis aux lieux de traitement de Google Cloud Platform (jusque-là Irlande), et le resserrement de l'obligation de notification aux seuls ajouts ou remplacements de sous-traitants ([mémo OTA](https://opentermsarchive.org/en/memos/mistral-operates-usa-no-notification/)). Source fiable mais ancienne, à recouper avec la liste actuelle **[à vérifier]**.

### 4.5 Conséquences pour le site

- Mistral est le sous-traitant (DPA automatique) pour l'audio et le texte du brief. À mentionner dans la politique de confidentialité : finalité, durée (30 jours chez Mistral, sauf ZDR), lieu (UE par défaut, transferts possibles encadrés par CCT).
- À faire sur le compte Mistral : passer en paiement à l'usage, activer l'opt-out d'entraînement, demander le ZDR (motif : données de prospects, site B2B, volume faible), s'abonner aux changements de sous-traitants.
- L'endpoint EU apporte un vrai engagement de lieu d'inférence pour 10 % de plus, soit moins de 0,002 $ par brief. À utiliser s'il fonctionne pour le temps réel.
- Par rapport à l'architecture Deepgram + Claude, un seul fournisseur, français, et le texte ne part plus chez Anthropic aux États-Unis.

---

## 5. Reformulation : quel modèle

Prix ([API pricing](https://docs.mistral.ai/inference/pricing)) :

| Modèle | ID | Entrée / Sortie (par M tokens) | Statut |
|---|---|---|---|
| Mistral Small 4 | `mistral-small-2603` | 0,15 $ / 0,60 $ | GA (16 mars 2026), 256k contexte, sorties structurées ([fiche](https://docs.mistral.ai/models/mistral-small-4-0-26-03)) |
| Mistral Large 4 | `mistral-large-4-0` | 0,70 $ / 2,10 $ | GA (5 novembre 2026 ; preview depuis le 6 octobre), 1M contexte ([fiche](https://docs.mistral.ai/models/mistral-large-4-0)) |
| Ministral 3 14B | — | 0,20 $ / 0,20 $ | GA (décembre 2025) |
| Mistral Medium 3.5 | `mistral-medium-3-5` | — | **Déprécié** au 31 octobre 2026, remplacé par Large 4 ([fiche](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)) |

- **Recommandation : Mistral Small 4.** Réécrire ~400 mots en quatre rubriques (Contexte / Ce qui coince / Ce que vous souhaitez / À préciser) est une tâche simple. Les sorties structurées (schéma JSON) garantissent les rubriques. C'est un modèle hybride (instruct + raisonnement) : garder le raisonnement au minimum. Le nom exact du paramètre (`reasoning_effort` ?) n'est pas documenté sur sa fiche **[à vérifier]**. Pour Large 4, `reasoning_effort="none"` renvoie une erreur 400 depuis le 29 octobre 2026 ; seules `low`, `medium` et `high` sont acceptées ([changelog](https://docs.mistral.ai/resources/changelogs)).
- Repli : Large 4 si la qualité de Small 4 déçoit sur des briefs réels. Le coût reste négligeable.
- Disponibilité de Small 4 sur l'endpoint EU : **[à vérifier via `models.list`]**.

---

## 6. Coût par brief

Hypothèses : 2 min de dictée ; 400 mots en français ≈ 550 tokens ; prompt système ≈ 500 tokens ; entrée ≈ 1 100 tokens, sortie ≈ 600 tokens (400 mots structurés).

| Poste | Calcul | Coût |
|---|---|---|
| Dictée (`voxtral-mini-transcribe-realtime-3`) | 2 min × 0,008 $ | 0,016 $ |
| Reformulation Small 4 | 1 100 × 0,15 + 600 × 0,60 (par M) | ≈ 0,0005 $ |
| Reformulation Large 4 (repli) | 1 100 × 0,70 + 600 × 2,10 (par M) | ≈ 0,002 $ |
| **Total (Small 4)** | | **≈ 0,017 $** (≈ 0,018 $ avec l'endpoint EU, +10 %) |

Une reformulation refusée puis relancée double à peine le poste reformulation. Avec quelques briefs par semaine, la facture mensuelle reste sous 0,10 $. Un jeton de dictée détourné coûte au plus ≈ 0,12 $ (15 min).

---

## 7. Architecture recommandée

```
1. Prospect clique « Dicter » → POST /api/dictee/jeton (Astro, limité par IP)
      → Mistral POST /v1/client/sessions {purpose: "realtime", model: "voxtral-mini-transcribe-realtime-3"}
      → renvoie client_secret.value (rt_…, ~15 min)
2. Navigateur → WebSocket direct wss://api[.eu].mistral.ai/v1/audio/transcriptions/realtime?model=…
      sous-protocoles ["realtime", rt_…]
      session.update {language: "fr", target_streaming_delay_ms: 480–960, audio_format: pcm_s16le 16 kHz}
      AudioWorklet → Int16 → base64 → input_audio.append
      transcription.text.delta → ajouté au textarea
3. Prospect relit, corrige, demande la reformulation → POST /api/brief/reformuler (Astro)
      → Mistral chat completions, mistral-small-2603, sortie structurée (4 rubriques)
4. Prospect accepte ou refuse → POST /api/brief → Resend → Henri
```

**Avant de coder, un test de 30 minutes** (avec une clé payante) lève les incertitudes :
1. `models.list` sur `api.eu.mistral.ai` : `voxtral-mini-transcribe-realtime-3` et `mistral-small-2603` y sont-ils ?
2. `POST /v1/client/sessions` sur l'endpoint EU, puis un WebSocket avec le jeton `rt_*` et le modèle v3, depuis un navigateur.
3. Une dictée de 2 min en français : qualité à 480 et à 960 ms, pas d'erreur de fenêtre de contexte.

Si l'étape 2 échoue sur l'endpoint EU mais réussit sur le global : rester en connexion directe sur le global (hébergement UE par défaut, sans engagement contractuel de lieu d'inférence). Si les jetons `rt_*` ne marchent pas avec la v3 : relais par le serveur (§ 2.2), ou modèle 2602 tant qu'il n'est pas retiré.

---

## 8. Points non confirmés

- Le jeton `rt_*` fonctionne-t-il avec le modèle v3 (sa page est classée « Deprecated ») ?
- Le WebSocket temps réel et `/v1/client/sessions` existent-ils sur `api.eu.mistral.ai` ? La surcharge de 10 % s'applique-t-elle à l'audio ?
- Le ZDR couvre-t-il le WebSocket temps réel ?
- La liste des sous-traitants et leurs lieux (page Trust Center illisible par mes outils).
- Le texte exact de la politique de confidentialité sur les 30 jours (page non lisible, chiffre cité par les résultats de recherche).
- Le réglage par défaut de l'entraînement en paiement à l'usage.
- La liste des langues de la v3 temps réel et son WER en français ; la durée maximale d'une session.
- La date de retrait de `voxtral-mini-transcribe-realtime-2602`.
