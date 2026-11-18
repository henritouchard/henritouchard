# Recherche : obligations légales du site, de la dictée et de la mesure d'audience

Ticket : #13 (carte : #1). Date des relevés : 18 novembre 2026.

**Question.** Pour henritouchard.fr, site d'un développeur indépendant français (micro-entreprise / EI), auto-hébergé sur un VPS Hostinger, quelles obligations légales s'appliquent ? Cinq points :
1. les mentions légales obligatoires ;
2. le RGPD du brief (coordonnées envoyées par e-mail via Resend, brouillon en localStorage) ;
3. le RGPD de la dictée et de la reformulation (micro, Voxtral Realtime et Mistral Small sur `api.eu.mistral.ai`, aucun audio stocké) ;
4. la liste des sous-traitants (Mistral, Resend, Hostinger) et la localisation des données ;
5. les règles CNIL sur les traceurs : mesure d'audience exemptée de consentement, et statut du brouillon en localStorage.

> **Ce document n'est pas un avis juridique.** Chaque affirmation renvoie à sa source primaire. Mes interprétations sont marquées « lecture » ; les points qu'un juriste (ou la CNIL, via sa permanence) devrait valider sont marqués **[à faire valider]**, ceux que je n'ai pas pu lire à la source **[à vérifier]**.

---

## 1. Synthèse

| Sujet | Obligatoire | Recommandé |
|---|---|---|
| Mentions légales | Nom, prénom, adresse, téléphone, e-mail, numéro SIREN, directeur de publication, identité et coordonnées de l'hébergeur ; dénomination avec « EI » ; numéro de TVA s'il existe | Page dédiée « Mentions légales » liée en pied de page sur toutes les pages |
| Brief (formulaire + e-mail) | Information RGPD (art. 13) au point de collecte et dans une politique de confidentialité ; durée de conservation définie ; registre des traitements | Base légale « mesures précontractuelles » ; conservation 3 ans après le dernier contact ; adresse dédiée |
| Brouillon en localStorage | Le localStorage est un « traceur » au sens de la CNIL ; exempté s'il est strictement nécessaire au service demandé (lecture) | Le mentionner dans la politique de confidentialité ; l'effacer à l'envoi ; bouton « effacer le brouillon » |
| Dictée et reformulation | Information avant l'ouverture du micro ; Mistral cité comme sous-traitant | Clic explicite « Activer la dictée » avant la demande d'autorisation du navigateur ; compte payant, opt-out d'entraînement, ZDR demandé |
| Sous-traitants | DPA en place (art. 28) ; transferts hors UE encadrés et signalés (art. 13) | Région Resend `eu-west-1` ; VPS Hostinger en France ou en Allemagne |
| Mesure d'audience | Sans consentement uniquement si la solution respecte les critères d'exemption CNIL ; sinon bannière | Matomo auto-hébergé en mode CNIL, ou analyse des journaux du serveur ; pas de Google Analytics |
| Code de la consommation | Ne s'applique pas aux prospects visés (des entreprises) — sauf cas limites (§ 7) | Pas de médiateur à afficher tant que l'offre reste B2B **[à faire valider]** |

**Bonne nouvelle :** avec une mesure d'audience exemptée et un brouillon strictement fonctionnel, **le site peut se passer de bannière de cookies**.

---

## 2. Mentions légales

### 2.1 Ce que dit la loi

- **LCEN, article 1-1, I** (en vigueur depuis le 23 mai 2024, créé par la loi n° 2024-449 dite SREN) : toute personne qui édite un service de communication au public en ligne met à disposition, « dans un standard ouvert » ([Légifrance, LCEN art. 1-1](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000049568614)) :
  - personne physique : **nom, prénoms, domicile, numéro de téléphone** et, si elle y est soumise, **numéro d'immatriculation** ;
  - le nom du **directeur de la publication** ;
  - le nom, la dénomination ou raison sociale, **l'adresse et le téléphone de l'hébergeur** ;
  - le cas échéant, l'identité et l'adresse de toute personne qui stocke les données traitées directement pour l'édition du service.
- L'anonymat (II du même article) est réservé à l'éditeur « à titre non professionnel ». **Il ne s'applique pas ici** : le site a un but commercial.
- **LCEN, article 19** (en vigueur depuis le 1er juillet 2016) : toute personne exerçant le commerce électronique offre un accès « facile, direct et permanent » à : nom et prénoms ; adresse d'établissement, **adresse électronique** et téléphone ; numéro RCS ou RM le cas échéant ; **numéro de TVA intracommunautaire** si elle en a un ; autorité d'autorisation ou règles de la profession réglementée le cas échéant ([Légifrance, LCEN art. 19](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000032236011)).
- L'article 14 de la LCEN définit le commerce électronique de façon large : il inclut les services qui fournissent des informations en ligne et des communications commerciales, « y compris lorsqu'ils ne sont pas rémunérés par ceux qui les reçoivent » ([Légifrance, LCEN art. 14](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000006421558)). Lecture : un site vitrine qui sollicite des leads entre dans ce champ ; l'article 19 s'applique donc.

### 2.2 Ce qui change selon le statut

- **Entrepreneur individuel (toute EI, y compris la micro-entreprise)** : depuis la réforme de 2022, l'EI utilise une dénomination qui incorpore son nom, « précédé ou suivi immédiatement » des mots « entrepreneur individuel » ou des initiales « EI ». Cette dénomination figure sur les documents et correspondances professionnels ([Légifrance, C. com. art. R526-27](https://www.legifrance.gouv.fr/codes/id/LEGIARTI000046573109/2022-11-19)). Lecture : le site étant un document professionnel, afficher **« Henri Touchard EI »** dans les mentions légales (et sur devis et factures).
- **Immatriculé au RCS** (commerçant) : le site doit aussi porter la mention « RCS » suivie de la ville du greffe, le numéro unique d'identification (SIREN) et l'adresse du siège ; amende de 4e classe en cas de manquement ([Légifrance, C. com. art. R123-237](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000023379456/)). Un développeur en activité libérale relève normalement du seul registre national des entreprises (RNE), pas du RCS : cette règle ne s'applique alors pas à la lettre, mais le **SIREN** reste dû au titre de l'« immatriculation » de l'art. 1-1 LCEN **[à faire valider : statut exact d'Henri — libéral BNC ou commercial BIC]**.
- **Micro-entreprise en franchise de TVA** : pas de numéro de TVA intracommunautaire à afficher si Henri n'en a pas (art. 19, 4°, « s'il en a un »). La mention « TVA non applicable, art. 293 B du CGI » concerne les factures, pas le site.
- **Domicile** : l'art. 1-1 exige le « domicile » d'une personne physique. Si Henri ne veut pas afficher son adresse personnelle, la solution habituelle est une **domiciliation d'entreprise** déclarée comme adresse d'établissement **[à faire valider : suffisance d'une adresse de domiciliation au regard du mot « domicile »]**.
- **Directeur de la publication** : Henri lui-même.

### 2.3 Concrètement, la page « Mentions légales »

1. Éditeur : Henri Touchard EI, adresse, téléphone, e-mail, SIREN, (TVA intracommunautaire si existante).
2. Directeur de la publication : Henri Touchard.
3. Hébergeur : Hostinger (entité contractante indiquée sur la facture ; le DPA cite Hostinger International Ltd., 61 Lordou Vironos str., 6023 Larnaca, Chypre — [Hostinger DPA](https://www.hostinger.com/legal/dpa)) + **numéro de téléphone de l'hébergeur** **[à vérifier : le numéro de Hostinger International n'est pas dans le DPA ; à relever sur le site de Hostinger]**.
4. Lien vers la politique de confidentialité (peut être sur la même page).

---

## 3. RGPD du brief

### 3.1 Responsable de traitement et base légale

- Henri est **responsable de traitement** ; Mistral, Resend et Hostinger sont ses **sous-traitants** (art. 28 RGPD), voir § 5.
- Base légale proposée pour le brief : **mesures précontractuelles prises à la demande de la personne** (RGPD art. 6.1.b, [EUR-Lex](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679)). Le prospect demande un devis : traiter son message pour y répondre en découle directement. Lecture, **[à faire valider]**.
- Prospection ultérieure (relancer un prospect, lui envoyer des nouvelles) : en B2B, l'**intérêt légitime** suffit si le message est en rapport avec la profession de la personne, avec un **droit d'opposition simple** à chaque envoi ([CNIL, prospection par courrier électronique](https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique)).

### 3.2 Information (art. 13 RGPD) — obligatoire

Au point de collecte (dans la modale, une ligne + lien) et dans la politique de confidentialité : identité du responsable, finalité, base légale, destinataires (sous-traitants), transferts hors UE et leurs garanties, durée de conservation, droits (accès, rectification, effacement, opposition, limitation, portabilité), droit de réclamation auprès de la CNIL ([EUR-Lex, RGPD art. 13](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679)).

### 3.3 Durée de conservation

- Le référentiel CNIL « gestion des activités commerciales » (non contraignant, mais référence) : les données d'un **prospect non client** peuvent être conservées **3 ans à compter de la collecte ou du dernier contact émanant du prospect** ; à l'issue, on le recontacte ou on supprime. Pour un client : durée de la relation + 3 ans ([CNIL, référentiel gestion commerciale](https://www.cnil.fr/sites/cnil/files/atoms/files/referentiel_traitements-donnees-caractere-personnel_gestion-activites-commerciales.pdf) ; [CNIL, Q/R sur les référentiels](https://www.cnil.fr/fr/questions-reponses-sur-les-referentiels-relatifs-la-gestion-des-activites-commerciales-et-des)).
- Concrètement, le lead vit dans la boîte mail d'Henri : c'est là que s'applique la purge à 3 ans **[recommandé]**.

### 3.4 Registre des traitements — obligatoire en pratique

La dérogation des moins de 250 salariés ne couvre pas les traitements **non occasionnels**, et la CNIL cite justement « la gestion des clients, prospects » ([CNIL, registre](https://www.cnil.fr/fr/RGPD-le-registre-des-activites-de-traitement)). Henri doit donc tenir un registre simple (le modèle CNIL suffit) avec : leads du site, dictée/reformulation, mesure d'audience, journaux du serveur.

### 3.5 Brouillon en localStorage

Voir § 6.3 (traceurs). Côté RGPD : le brouillon reste sur l'appareil du prospect et n'est transmis à personne tant qu'il n'envoie pas. **[recommandé]** l'effacer à l'envoi réussi et proposer un bouton pour le supprimer.

### 3.6 Journaux du serveur (Caddy)

Les adresses IP des journaux d'accès sont des données personnelles. **[recommandé]** les mentionner dans la politique (finalité : sécurité ; base : intérêt légitime) et fixer une rotation courte (ex. quelques semaines à 6 mois) **[à faire valider : durée]**.

---

## 4. RGPD de la dictée et de la reformulation

### 4.1 Nature des données

- La voix est une donnée personnelle. Elle ne devient une **donnée biométrique** (catégorie particulière, art. 9) que si elle fait l'objet d'un « traitement technique spécifique » permettant ou confirmant l'**identification unique** de la personne (RGPD art. 4.14, [EUR-Lex](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679)). Une transcription en texte n'identifie personne : lecture, **pas d'art. 9** ici. Vérifier que la diarisation de Voxtral (séparation des locuteurs) reste désactivée, par prudence **[recommandé]**.
- Le contenu dicté peut, lui, contenir n'importe quoi (noms, données de tiers) : c'est un message libre, comme un e-mail.

### 4.2 Base légale et action positive

- La dictée est **facultative** : le prospect peut taper son brief. Base proposée : la même que le brief (6.1.b), la dictée n'étant qu'un mode de saisie demandé par la personne ; l'alternative prudente est le **consentement** (6.1.a), recueilli par le clic sur « Activer la dictée » **[à faire valider : choix entre 6.1.b et 6.1.a]**.
- Dans les deux cas, l'**ordre** compte :
  1. un encart d'information visible **avant** que le micro s'ouvre (déjà prévu, cf. #8) : « Votre voix est transcrite en direct par Mistral AI (serveurs dans l'UE). Aucun enregistrement n'est conservé sur ce site. Le texte reste modifiable. » + lien vers la politique ;
  2. un **clic explicite** de l'utilisateur sur « Activer la dictée » ;
  3. seulement alors, l'appel à `getUserMedia` (la demande d'autorisation du navigateur), puis la demande de jeton éphémère.
- La reformulation est proposée d'office (cf. #8) : elle envoie le texte à Mistral Small. L'information doit le dire, et le prospect garde le choix d'**accepter ou refuser** le résultat ; s'il ne veut pas que le texte parte chez Mistral, il faut un moyen de passer l'étape **[à faire valider : la reformulation « d'office » envoie le texte avant tout choix ; envisager « Reformuler » sur clic, ou l'annoncer clairement dans l'encart]**.

### 4.3 Ce que la politique de confidentialité doit dire sur Mistral

D'après la recherche #11 ([docs/research/voxtral.md](https://github.com/henritouchard/henritouchard/blob/research/voxtral/docs/research/voxtral.md), § 4) :
- Mistral AI (France) est sous-traitant ; DPA intégré aux conditions (version du 27 juillet 2026), CCT 2021/914 pour d'éventuels transferts ([Mistral DPA](https://legal.mistral.ai/terms/data-processing-addendum/)).
- Lieu : UE garanti par `api.eu.mistral.ai` ; **non documenté pour le WebSocket temps réel [à vérifier par le test prévu en #11]**. Si le test échoue et que l'endpoint global est utilisé, la politique doit dire « hébergé dans l'UE par défaut, transferts possibles encadrés par CCT ».
- Conservation : 30 jours glissants chez Mistral (surveillance des abus), sauf ZDR accordé.
- Réserve du DPA : Mistral est **responsable de traitement** pour la surveillance des abus et pour l'entraînement « unless Customer is or has opted-out » (§ 2.3). D'où, **obligatoire en pratique** pour rester cohérent avec l'information donnée : compte payant + opt-out d'entraînement activé ; **recommandé** : demander le ZDR.
- « Aucun audio stocké » est vrai **sur le VPS** (connexion directe navigateur → Mistral) ; ce n'est pas garanti chez Mistral sans ZDR. Formuler l'information en conséquence.

### 4.4 Règlement IA (AI Act)

Lecture rapide, **[à faire valider]** : la transcription et la reformulation ne sont pas des systèmes à haut risque. L'obligation de transparence de l'art. 50 (dire à l'utilisateur qu'il interagit avec une IA / marquer les contenus générés) est de toute façon satisfaite par l'interface, qui présente explicitement la reformulation « par l'IA ». Je n'ai pas approfondi ce point.

---

## 5. Sous-traitants et localisation

| Sous-traitant | Rôle | Données | Localisation | Garanties | Sources |
|---|---|---|---|---|---|
| **Mistral AI** (France) | Dictée (Voxtral Realtime), reformulation (Mistral Small) | Audio, texte du brief | UE via `api.eu.mistral.ai` (à confirmer pour le temps réel) ; données de compte possiblement hors région | DPA auto, CCT ; sous-traitants ultérieurs sur [trust.mistral.ai/subprocessors](https://trust.mistral.ai/subprocessors) (**page illisible par mes outils [à vérifier]**), objection sous 10 jours | [DPA](https://legal.mistral.ai/terms/data-processing-addendum/), [Regional inference](https://docs.mistral.ai/inference/regional-inference) |
| **Resend** (États-Unis) | Envoi de l'e-mail de lead | Coordonnées et brief (dans l'e-mail) | Envoi depuis la région choisie (`eu-west-1` = Irlande possible) ; mais **toutes les données de compte, métadonnées d'e-mails, logs et enregistrements d'API restent aux États-Unis**, quelle que soit la région ; DPA : traitements principaux aux États-Unis | CCT 2021/914 + certification **EU-US Data Privacy Framework** (DPA § 6, § 11) ; préavis de 14 jours sur les changements de sous-traitants ; 22 sous-traitants ultérieurs, tous listés aux États-Unis (AWS, Anthropic, Google, Supabase…) | [DPA Resend](https://resend.com/legal/dpa) (31 déc. 2025), [Subprocessors](https://resend.com/legal/subprocessors), [Regions](https://resend.com/docs/dashboard/domains/regions) |
| **Hostinger** | Hébergement du VPS (site, émission des jetons, journaux) | Journaux, requêtes, coordonnées en transit | VPS en Europe : **France, Allemagne, Lituanie, Royaume-Uni** (choisi à la création, fixe ensuite ; ville française non précisée) | DPA : Hostinger sous-traitant ; CCT modules 2 et 3 pour les transferts ; sous-traitants ultérieurs : AWS EMEA, Google Cloud EMEA, Cloudflare, MailChannels, Proofpoint, Anthropic Ireland, spectra tech, Vonage ; préavis de 10 jours | [DPA Hostinger](https://www.hostinger.com/legal/dpa) (révisé le 29 sept. 2026), [Server locations](https://www.hostinger.com/support/1583267-where-are-hostinger-servers-located/) (17 nov. 2026) |

**À faire :**
- **[obligatoire]** Accepter/archiver les trois DPA (Mistral et Resend s'appliquent par acceptation des conditions ; Hostinger aussi) et les citer dans le registre.
- **[obligatoire]** Mentionner dans la politique de confidentialité le **transfert vers les États-Unis** par Resend et sa garantie (DPF + CCT).
- **[recommandé]** Choisir la région Resend `eu-west-1` (l'envoi part d'Irlande) — sans illusion : les métadonnées restent aux États-Unis.
- **[recommandé]** Réduire ce qui transite par Resend : l'e-mail de lead part vers Henri seul (pas d'accusé de réception au prospect contenant le brief), et purger les logs Resend si l'option existe **[à vérifier]**.
- **[recommandé]** VPS en **France** (ou Allemagne) pour garder l'hébergement dans l'UE ; éviter le Royaume-Uni (adéquation, mais hors UE).
- **[recommandé]** S'abonner aux notifications de changements de sous-traitants des trois fournisseurs.
- Le site **ne doit pas** dépendre de ressources tierces chargées par le navigateur (polices Google Fonts, CDN) sans les auto-héberger : chaque requête transmet l'IP du visiteur au tiers. Lecture, recommandé.

---

## 6. Traceurs (cookies, localStorage) et mesure d'audience

### 6.1 Le principe

- Article 82 de la loi Informatique et Libertés : tout accès ou stockage dans le terminal exige le consentement, sauf s'il a pour finalité exclusive de permettre la communication électronique, ou s'il est **strictement nécessaire à un service expressément demandé** par l'utilisateur ([CNIL, que dit la loi](https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies/que-dit-la-loi)).
- Les lignes directrices CNIL (délibération n° 2020-091) visent explicitement « le « local storage » mis en œuvre au sein du standard HTML 5 » (§ 13), ainsi que le **fingerprinting** ([CNIL, lignes directrices](https://www.cnil.fr/sites/cnil/files/atoms/files/lignes_directrices_de_la_cnil_sur_les_cookies_et_autres_traceurs.pdf)). Le localStorage est donc un traceur au sens de l'article 82.

### 6.2 Mesure d'audience exemptée de consentement

Lignes directrices § 50-52 et page CNIL (4 juillet 2025) ([CNIL, solutions de mesure d'audience](https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies-solutions-pour-les-outils-de-mesure-daudience)) :
- **Conditions (obligatoires)** : finalité limitée à la mesure d'audience **pour le compte exclusif de l'éditeur** ; production de **statistiques anonymes** uniquement ; pas de suivi de la navigation sur d'autres sites ; pas de recoupement avec d'autres traitements ; pas de transmission à des tiers.
- **Recommandations** : informer (politique de confidentialité) ; durée de vie des traceurs ≈ **13 mois** sans prolongation automatique ; conservation des données **25 mois** maximum ; vigilance sur les transferts hors UE.
- La CNIL ne publie plus de liste nominative de solutions ; elle fournit un **outil d'auto-évaluation** aux éditeurs de solutions, qui doivent remettre une documentation de conformité.
- La mesure d'audience reste un traitement soumis au RGPD (§ 52) : à inscrire au registre et dans la politique.

**Options pour le site :**

| Option | Consentement ? | Commentaire |
|---|---|---|
| **Matomo auto-hébergé, « mode CNIL »** | Non, si configuré | Le mode CNIL masque 3 octets d'IP, limite le cookie à 13 mois, la conservation à ~25 mois, désactive User ID, heatmaps, A/B tests ; à compléter par un opt-out visible ([Matomo, FAQ CNIL](https://matomo.org/faq/how-to/how-do-i-configure-matomo-without-tracking-consent-for-french-visitors-cnil-exemption/)). Recommandation principale. |
| **Analyse des journaux du serveur** (ex. GoAccess sur les logs Caddy) | Non : rien n'est lu ni écrit dans le terminal, l'article 82 ne s'applique pas (lecture) | RGPD seul (IP dans les logs) ; moins précis (robots), mais aucun script. Bonne option minimale. |
| Outils « sans cookie » (Plausible, Umami…) | Probablement non si les critères sont respectés | Attention : un identifiant calculé (hash IP + navigateur) peut être vu comme du fingerprinting, que la CNIL range parmi les traceurs ; vérifier la documentation d'exemption de l'éditeur **[à faire valider]**. Version SaaS : vérifier la localisation. |
| Google Analytics | **Oui** | Données réutilisées par Google, transferts hors UE : hors exemption. À écarter. |

Le **suivi de conversion** (lead envoyé) peut se faire dans Matomo en événement, sans quitter l'exemption tant qu'il reste anonyme et pour le seul compte d'Henri (lecture).

### 6.3 Le brouillon du brief en localStorage

- La liste d'exemptions des lignes directrices (§ 49) ne cite pas les formulaires, mais cite par analogie « garder en mémoire le contenu d'un panier d'achat ». Le critère est la finalité, pas la technique ([CNIL, que dit la loi](https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies/que-dit-la-loi)).
- Lecture : un brouillon que le prospect est en train de rédiger, conservé uniquement pour qu'il retrouve son texte, sert un service **expressément demandé** (écrire et envoyer un brief) ; il est **exempté de consentement**, à condition de :
  - ne servir qu'à ça (aucune lecture à d'autres fins, aucune transmission) ;
  - **[recommandé]** être effacé à l'envoi et avoir une durée de vie limitée (ex. 7 à 30 jours) ;
  - **[recommandé]** être mentionné dans la politique de confidentialité.
- **[à faire valider]** : la CNIL n'a pas de position écrite sur ce cas précis.

### 6.4 Conséquence : pas de bannière

Si le site se limite au brouillon et à une mesure d'audience exemptée, **aucune bannière de consentement n'est requise**. Une simple mention dans la politique de confidentialité et un lien d'opposition à la mesure d'audience suffisent. Toute brique ajoutée plus tard (vidéo YouTube intégrée, widget LinkedIn, pixel publicitaire, chat tiers) ferait basculer dans l'obligation de consentement.

---

## 7. Code de la consommation

- Les prospects visés sont des entreprises (startups, scale-ups, PME : cf. GLOSSARY). Les obligations d'information précontractuelle (C. conso L111-1, L221-5), le droit de rétractation de 14 jours (L221-18, [Légifrance](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032226842)) et la **médiation de la consommation** (L612-1 : tout consommateur a droit à un médiateur gratuit, que le professionnel doit afficher, [economie.gouv.fr](https://www.economie.gouv.fr/mediation-conso/vous-etes-un-professionnel/vos-principales-obligations)) visent les relations avec des **consommateurs**. Lecture : **non obligatoires** tant que l'offre reste B2B.
- **Cas limites [à faire valider]** :
  - un particulier qui envoie un brief pour un besoin personnel deviendrait un consommateur ; si Henri accepte, les règles conso et l'obligation d'adhérer à un médiateur s'appliquent. **Recommandé** : écrire sur le site que l'offre s'adresse aux professionnels ;
  - l'article L221-3 étend certaines protections conso (information, rétractation) aux **professionnels de 5 salariés ou moins**, pour un contrat **conclu hors établissement** dont l'objet sort de leur activité principale ([analyse Centre Inffo](https://www.centre-inffo.fr/?p=513198)). Une très petite entreprise qui signe un devis lors d'un « diagnostic sur place » (cf. #6) pourrait en relever. Concerne les devis et CGV, pas le site lui-même.
- Entre professionnels : CGV à communiquer à tout acheteur qui les demande (C. com. L441-1) — sujet des devis, hors site **[à vérifier, non relu]**.

---

## 8. Liste d'actions pour le site

**Obligatoire**
1. Page « Mentions légales » (§ 2.3) : Henri Touchard EI, adresse, téléphone, e-mail, SIREN, directeur de la publication, Hostinger avec adresse et téléphone.
2. Politique de confidentialité (même page possible) : brief, dictée/reformulation, e-mail de lead, journaux serveur, mesure d'audience, brouillon local ; sous-traitants, transfert États-Unis (Resend), durées, droits, CNIL.
3. Mention courte au point de collecte dans la modale du brief, et encart d'information **avant** l'ouverture du micro, suivi d'un clic explicite.
4. Mesure d'audience **dans le cadre de l'exemption CNIL** (Matomo mode CNIL ou logs), ou bien bannière de consentement.
5. Compte Mistral payant + opt-out d'entraînement (sinon l'information « Mistral sous-traitant » est fausse).
6. Registre des traitements (modèle CNIL).
7. Dénomination « EI » sur le site, les devis et les factures.

**Recommandé**
- ZDR demandé à Mistral ; endpoint `api.eu.mistral.ai` confirmé par le test de #11.
- Resend en `eu-west-1` ; VPS Hostinger en France.
- Brouillon effacé à l'envoi, durée de vie limitée, bouton « effacer ».
- Conservation des leads : 3 ans après le dernier contact.
- Rotation des journaux Caddy ; polices et scripts auto-hébergés.
- Mention « offre réservée aux professionnels ».

---

## 9. Points à faire valider (juriste, expert-comptable ou CNIL)

1. Statut exact d'Henri (libéral/RNE ou commercial/RCS) et mentions qui en découlent (§ 2.2).
2. Adresse de domiciliation à la place du domicile personnel (§ 2.2).
3. Base légale de la dictée : 6.1.b ou consentement (§ 4.2).
4. Reformulation proposée d'office : le texte part chez Mistral avant tout choix explicite (§ 4.2).
5. Exemption du brouillon en localStorage (§ 6.3).
6. Outils « sans cookie » à identifiant calculé et fingerprinting (§ 6.2).
7. Cas des particuliers et de l'article L221-3 pour les très petites entreprises (§ 7).

**Non vérifié à la source** : liste des sous-traitants de Mistral (Trust Center illisible) ; téléphone de l'entité Hostinger ; option de purge des logs Resend ; texte de L441-1 C. com. ; WebSocket temps réel sur `api.eu.mistral.ai` (test de #11).
