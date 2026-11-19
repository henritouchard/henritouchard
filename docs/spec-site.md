# Spec du site henritouchard.fr

État **final** des décisions de la carte [Site henritouchard.fr : spec orientée leads](https://github.com/henritouchard/henritouchard/issues/1). Chaque point renvoie au ticket qui le tranche ; l'historique des révisions reste dans les tickets. Vocabulaire : [`GLOSSARY.md`](../GLOSSARY.md).

**Seul objectif du site** : générer des **leads** (briefs, briefs interrompus et demandes de rappel) de missions freelance, auprès de prospects français (startups, scale-ups, PME, tous secteurs). Site en français, marché France uniquement.

---

## 1. Positionnement et messages

- **Offre** : l'optimisation opérationnelle. Henri pose un regard extérieur, opérationnel et technique, repère les points de friction et conçoit, construit et maintient les outils sur mesure qui les suppriment. L'IA est un moyen (« avec ou sans IA »), jamais l'offre. ([Quel message principal…](https://github.com/henritouchard/henritouchard/issues/5), [Quel référencement technique pour chaque page ?](https://github.com/henritouchard/henritouchard/issues/14), [Quelle identité visuelle…](https://github.com/henritouchard/henritouchard/issues/15))
- **Intitulé** (surtitre, un seul) : « Optimisation opérationnelle & outils sur mesure ». Ni « agence » ni « conseil ». ([Quel référencement technique pour chaque page ?](https://github.com/henritouchard/henritouchard/issues/14))
- **Titre (H1)** : « J'optimise vos processus là où ça compte, pour que votre équipe se concentre sur ce qui a de la valeur. » ([Quel message principal…](https://github.com/henritouchard/henritouchard/issues/5))
- **Sous-titre** : « Un regard extérieur, opérationnel et technique, sur votre fonctionnement : je repère les points de friction, puis je conçois et construis les outils sur mesure qui les suppriment, avec ou sans IA. Et j'en assure la maintenance dans la durée. » ([Quelle identité visuelle…](https://github.com/henritouchard/henritouchard/issues/15))
- **Ton** : « je » et vouvoiement ; message positif (on libère l'humain des tâches ingrates, on ne le remplace pas). Dans le haut de page, on dit « repérer », jamais « diagnostiquer » (le **Diagnostic** est une prestation). ([Quel message principal…](https://github.com/henritouchard/henritouchard/issues/5), [Quelle identité visuelle…](https://github.com/henritouchard/henritouchard/issues/15))
- **Mots** : « automatisation des processus » et « logiciel sur mesure » servent au référencement, jamais à nommer l'offre. « Product engineer », « développeur fullstack freelance », Fractional CTO et FDE n'apparaissent pas. ([Quel référencement technique pour chaque page ?](https://github.com/henritouchard/henritouchard/issues/14), [Vérifier connecté les volumes de recherche](https://github.com/henritouchard/henritouchard/issues/10))
- **Offre sans tarif** : ni TJM ni prix affiché. À la place : prix ferme connu avant de commencer, devis rapide, propriété du code et des outils livrés. ([Comment présenter l'offre…](https://github.com/henritouchard/henritouchard/issues/6))

## 2. Pages et contenu

### Pages de la V1

| Page | URL | Rôle |
|---|---|---|
| Accueil | `/` | l'offre, directe et explicite |
| Expériences et réalisations | `/realisations/` | liste des récits d'expérience |
| Récit | `/realisations/<slug-mot-clé>/` | un récit par expérience |
| À propos | `/a-propos/` | rassurer sur la personne |
| Mentions légales | `/mentions-legales/` | mentions légales + section `#confidentialite` (une seule page) |

Pas de page Contact, Services ni Brief. Barre oblique finale toujours présente. ([Quelle architecture de pages et quelle stack ?](https://github.com/henritouchard/henritouchard/issues/9), [Quel référencement technique pour chaque page ?](https://github.com/henritouchard/henritouchard/issues/14), réponse d'Henri du 2026-11-19 sur [Rassembler la spec du site](https://github.com/henritouchard/henritouchard/issues/31))

### Barre de navigation (fixe, sur toutes les pages)

Logo (retour à l'accueil), « Expériences et réalisations », « À propos », bouton « Décrivez votre besoin » toujours visible. Sur mobile : menu replié, le bouton du brief reste hors du menu. Fond encre nuit uni. ([Quelle architecture de pages…](https://github.com/henritouchard/henritouchard/issues/9), [Quelles réalisations deviennent les premiers récits…](https://github.com/henritouchard/henritouchard/issues/7), [La palette et les typographies…](https://github.com/henritouchard/henritouchard/issues/21))

### Accueil

Ordre des sections ; ni preuve ni présentation sur l'accueil, elles passent par la navigation. ([Quelle architecture de pages…](https://github.com/henritouchard/henritouchard/issues/9))

1. **Haut de page** (bande encre) : surtitre (intitulé) + filet ; grand titre à gauche (« là où ça compte » en corail) ; sous-titre et boutons à droite : « Décrivez votre besoin » (principal, ouvre le brief) et « Voir des réalisations » (secondaire). Dessous, la **chaîne en 3 maillons** : *Je repère* les points de friction → *Je construis* l'outil sur mesure qui les supprime → *Je le maintiens* dans la durée. ([Quelle identité visuelle…](https://github.com/henritouchard/henritouchard/issues/15), [La palette…](https://github.com/henritouchard/henritouchard/issues/21))
2. **Approche** : sommaire numéroté 01 à 05 : regard extérieur et analyse du fonctionnement ; l'humain sublimé ; propositions innovantes ; mesurable (temps gagné compté avant/après) ; adapté à vous (l'outil s'adapte à votre façon de travailler). ([Quel message principal…](https://github.com/henritouchard/henritouchard/issues/5))
3. **Points de friction** : 3 ou 4 scènes génériques en **tickets** (`friction-0n`, « ● à optimiser »), dites avec les mots du prospect, sans anglicismes. Exemples : bons d'intervention papier ressaisis le soir ; mêmes données ressaisies dans plusieurs outils ; bilan de la semaine monté à la main ; demandes reçues par mail recopiées à la main. Chacun mène au brief (« Ça vous parle ? Décrivez votre besoin ») et, dès qu'il existe, à son récit, avec un lien au texte descriptif (jamais « en savoir plus »). ([Comment présenter l'offre…](https://github.com/henritouchard/henritouchard/issues/6), [Quel référencement technique…](https://github.com/henritouchard/henritouchard/issues/14))
4. **Comment je travaille** : 4 étapes en **circuit** : (1) **Échange** : votre brief, puis un appel ; (2) **Devis ou diagnostic** : devis au forfait gratuit pour un besoin cadré, sinon diagnostic sur place d'un nombre de jours convenu, facturé à la journée ; (3) **Construction** : livraisons régulières, première version mise en service pour un projet important ; (4) **Mise en service et mesure** (temps avant/après), puis la maintenance prend le relais (dernière étape en corail, pointillé vers la maintenance). Ensuite, un encadré « mes engagements » (prix ferme, devis rapide, propriété du code) et la durée : « Aucune durée minimale ni maximale : d'une demi-journée pour un besoin précis à plusieurs mois pour un projet important. » Maintenance : facultative, mensuelle, sans engagement long (surveillance, correctifs, mises à jour, petits ajustements) ; toute évolution = nouvelle mission. ([Comment présenter l'offre…](https://github.com/henritouchard/henritouchard/issues/6), [Quelle identité visuelle…](https://github.com/henritouchard/henritouchard/issues/15))
5. **Appel final** (bande encre, centré) vers le brief.

« Automatisation des processus » et « logiciel sur mesure » apparaissent au moins une fois en toutes lettres, dans un H2 ou dans les Points de friction, pas dans le haut de page ; formulation fixée à la rédaction. ([Quel référencement technique…](https://github.com/henritouchard/henritouchard/issues/14))

### Expériences et réalisations

- **Liste** façon Medium, de la plus récente à la plus ancienne. Chaque entrée : titre, chapeau, image, date, temps de lecture, cadre (mission, poste ou projet personnel). Pas de filtres en V1. Elle commence par une phrase qui rappelle l'offre (arrivées depuis Google). ([Quelles réalisations…](https://github.com/henritouchard/henritouchard/issues/7))
- **Récit** (format long, un article = une expérience) : (1) résumé en tête : friction → solution → résultat, en trois blocs reliés par des flèches ; (2) fiche (cadre, rôle, période, statut, stack) dans la marge gauche, fixe au défilement ; (3) le point de friction ; (4) la démarche ; (5) le système (captures, schémas) ; (6) le résultat, sans chiffre inventé ; (7) ce que j'en retiens ; (8) bandeau sombre d'appel au brief + liens vers 2 autres récits. En-tête centré, sections numérotées en mono. ([Quelles réalisations…](https://github.com/henritouchard/henritouchard/issues/7), [Quelle identité visuelle…](https://github.com/henritouchard/henritouchard/issues/15))
- **Récits prévus**, publiés au fil de l'eau sans attendre les missions pour des proches : PUM (en premier), Lizee (automatisation des commandes transporteurs), SambaÉdu v5 (Irundo), GTD (« charité bien ordonnée »). La rédaction se fait en binôme, hors spec. ([Quelles réalisations…](https://github.com/henritouchard/henritouchard/issues/7))
- Récits en Markdown/MDX dans le dépôt ; le frontmatter porte au moins `title`, `description` (condense le résumé), date de publication, `dateModified`, cadre et image. ([Quelle architecture…](https://github.com/henritouchard/henritouchard/issues/9), [Quel référencement technique…](https://github.com/henritouchard/henritouchard/issues/14), [Quels réglages techniques…](https://github.com/henritouchard/henritouchard/issues/12))

### À propos

Page courte, lue en moins d'une minute, qui rassure sans prouver. ([Que raconte l'« À propos » ?](https://github.com/henritouchard/henritouchard/issues/16))

1. Photo (portrait existant, recadré 4:5 sur le buste, couleur d'origine ; à côté de l'accroche sur ordinateur, au-dessus sur mobile) + accroche liée à l'offre. ([Quel style pour le portrait photo ?](https://github.com/henritouchard/henritouchard/issues/24))
2. Parcours en un ou deux paragraphes : IUT Techniques de commercialisation → Epitech → Lizee (développeur et Product Owner) → indépendant ; l'envie d'entreprendre comme moteur (« j'ai été à votre place ») ; séminaire de Versailles et IFF Europe en une phrase ; lien « Voir mes réalisations ».
3. « En dehors du code » : Le Bon Conseil d'abord, puis scoutisme, L'Arche, Graines en vie.
4. Appel au brief (seul passage vouvoyé).
5. Encart latéral : basé à Paris, sur place en Île-de-France, à distance partout en France ; 3 ou 4 stacks en texte, sans logos.
6. Lien « Ajouter à mes contacts » (voir pied de page).

Ton : première personne, direct, sans jargon. Écartés : frise, CV en PDF, mur de technologies, liens visibles vers LinkedIn et Malt.

### Pied de page (toutes les pages)

- Lien vers les mentions légales.
- Lien **GitHub discret** (peu parlant pour un dirigeant de PME). **Pas de lien visible vers LinkedIn ni Malt** : ils restent dans le `sameAs` de `Person`. (Réponse d'Henri du 2026-11-19 sur [Rassembler la spec du site](https://github.com/henritouchard/henritouchard/issues/31), qui tranche entre [Quel référencement technique…](https://github.com/henritouchard/henritouchard/issues/14) et [Que raconte l'« À propos » ?](https://github.com/henritouchard/henritouchard/issues/16))
- **Fiche contact** : lien « Ajouter à mes contacts », aussi présent sur À propos, affiché **seulement sur appareil tactile** (détecté par le type de pointeur, pas par la largeur). La vCard est **fabriquée au clic sur l'appareil**, à partir d'un numéro découpé en morceaux : le numéro n'apparaît jamais en clair, ni dans le code des pages ni dans un `.vcf` sur le serveur. Six champs : Henri Touchard, « Optimisation opérationnelle », téléphone pro, e-mail pro, henritouchard.fr, LinkedIn ; portrait en photo (jamais la tuile du logo). Ni captcha ni piège à robots, aucune donnée collectée. ([Comment ajouter le contact d'Henri…](https://github.com/henritouchard/henritouchard/issues/30))

## 3. Brief et demande de rappel

Le parcours décidé dans [Comment découper le brief en étapes guidées ?](https://github.com/henritouchard/henritouchard/issues/32), qui révise [Comment se comporte le brief…](https://github.com/henritouchard/henritouchard/issues/8) et, pour la demande de rappel, [Comment mesurer les leads…](https://github.com/henritouchard/henritouchard/issues/17). Le site produit trois types de leads : le **brief**, le **brief interrompu** et la **demande de rappel** (voir `GLOSSARY.md`). Prototype de référence (variante A) : [`prototypes/brief/brief-guide-prototype.html` sur la branche `prototype/brief`](https://github.com/henritouchard/henritouchard/blob/prototype/brief/prototypes/brief/brief-guide-prototype.html).

### Ouverture et brouillon

- Tous les boutons « Décrivez votre besoin » (navigation, haut de page, points de friction, appel final, fin de récit, À propos) ouvrent la même **modale centrée** (plein écran sur mobile), qui apparaît en fondu en glissant de 8 px. ([Quelle architecture…](https://github.com/henritouchard/henritouchard/issues/9), [Quels principes de mouvement…](https://github.com/henritouchard/henritouchard/issues/22))
- La modale s'ouvre aussi quand l'adresse se termine par `#brief`. Pas d'adresse `/brief` ni de redirection Caddy. ([Quel référencement technique…](https://github.com/henritouchard/henritouchard/issues/14), révision du 2026-11-18)
- **Brouillon en `localStorage`**, enregistré à chaque frappe : étape, coordonnées, préférence de contact, taille, texte sur la société, orientation, texte sur le besoin, état de la reformulation et ses 4 rubriques, indicateur « coordonnées déjà envoyées ». Effacé après un envoi réussi ou une demande de rappel, et au bout de 30 jours dans tous les cas. Au retour sur le site, la modale ne se rouvre pas seule : le bouton devient « Reprendre votre brief » et rouvre la modale à l'étape en cours. ([Quelle architecture…](https://github.com/henritouchard/henritouchard/issues/9), [Comment découper le brief…](https://github.com/henritouchard/henritouchard/issues/32))

### Parcours : 4 étapes, coordonnées d'abord

Barre de progression en haut de la modale ; lien « ← Retour » à partir de l'étape 2. Les coordonnées viennent en premier parce que l'abandon se produit surtout devant la page blanche : Henri garde le contact même si le prospect ne va pas au bout. ([Comment découper le brief…](https://github.com/henritouchard/henritouchard/issues/32))

1. **Vos coordonnées** : Nom et prénom \*, Société \*, E-mail \*, Téléphone (facultatif), puis « Je préfère être recontacté·e par e-mail / par téléphone ». Bouton **« Valider »**. Texte d'aide : les coordonnées servent aussi à recontacter le prospect s'il ne termine pas ; **formulation à reprendre** dans un ton professionnel, adapté à des PME traditionnelles (sans « rien n'est envoyé sans clic », qui va de soi).
   - **Préférence de contact** : « par e-mail » coché par défaut. Si le prospect remplit le téléphone sans avoir choisi lui-même, la coche passe sur « par téléphone ». Dès qu'il clique sur un choix, ce choix n'est plus modifié automatiquement. Tant que le téléphone est vide, « par téléphone » est grisé, et le vider ramène la coche sur « par e-mail ».
   - **Bouton secondaire** à côté de « Valider » : « Pas le temps de rédiger ? Rappelez-moi » (formulation à reprendre dans le même ton). Actif seulement quand les champs obligatoires **et le téléphone** sont remplis ; sinon grisé, avec l'indication « Indiquez votre numéro pour être rappelé·e. » Voir [Demande de rappel](#demande-de-rappel).
2. **Votre société** : « Décrivez brièvement votre société : votre activité, la taille de l'entreprise et, si c'est pertinent, votre façon de travailler dans les grandes lignes. » Taille facultative, en pastilles (Seul·e, 2 à 10, 11 à 50, 51 à 250, Plus de 250) ; texte requis (quelques mots) ; dictée proposée.
3. **Pourquoi m'appelez-vous ?** : « Où en êtes-vous ? » en trois choix : *J'ai un problème précis à régler* (devis gratuit au forfait), *Je sais où ça coince, pas comment le résoudre* (un diagnostic sur place peut être utile), *Une envie d'optimiser, encore floue*. Puis un texte requis (quelques phrases), dont l'exemple d'aide change selon le choix, avec « Pas besoin que ce soit bien écrit… » et la dictée.
4. **Relire et envoyer** : récapitulatif des deux textes et bouton « Reformuler » facultatif (rien ne part chez Mistral sans ce clic). La reformulation **fusionne les deux textes** en Contexte / Ce qui coince / Ce que vous souhaitez / À préciser. Elle est **modifiable sur place** : chaque rubrique garde son titre et sa mise en forme, et son texte est un champ sans bordure qui ressemble à du texte (contour au survol, hauteur qui suit le contenu). La version affichée, modifiée ou non, est celle qui est envoyée ; le lien « Revenir à mon texte » l'écarte. Pas de bouton « C'est ça, utiliser cette version ».

### Dictée

- Proposée aux étapes 2 et 3. Le bouton « Dicter » n'apparaît pas sans micro. Pas de fenêtre ni de clic de confirmation avant le micro : la demande d'autorisation du navigateur suffit. Micro bloqué : message invitant à écrire ou à réautoriser le micro dans le navigateur. ([Comment se comporte le brief…](https://github.com/henritouchard/henritouchard/issues/8), [Quelles mentions légales…](https://github.com/henritouchard/henritouchard/issues/18))
- Transcription en direct : bandeau « Je vous écoute… » ; chaque morceau finalisé s'ajoute au texte, que le prospect peut modifier. (Voxtral renvoie des deltas définitifs, jamais corrigés : pas de mots provisoires à remplacer.) ([Comment se comporte le brief…](https://github.com/henritouchard/henritouchard/issues/8), [Voxtral Realtime en français…](https://github.com/henritouchard/henritouchard/issues/11))
- **Encart d'information** près du micro et du bouton « Reformuler » : dictée et reformulation traitées par Mistral, en France, conservées 30 jours ; lien vers `/mentions-legales/#confidentialite`. ([Quelles mentions légales…](https://github.com/henritouchard/henritouchard/issues/18))

### Envoi des coordonnées et brief interrompu

([Comment découper le brief…](https://github.com/henritouchard/henritouchard/issues/32))

- Les coordonnées partent chez Henri **dès le clic sur « Valider »** (e-mail « Nouveau contact »). Si la modale est fermée à l'étape 1, avant « Valider », rien ne part.
- Si le prospect ferme la modale après « Valider » sans avoir envoyé son brief, il voit : « Pas le temps, ou pas l'envie, de compléter votre demande ? Je peux vous rappeler sous 48 h ouvrées pour en parler. Votre brouillon reste enregistré sur cet appareil si vous souhaitez le reprendre plus tard. » Suivent la case « Joindre ce que j'ai déjà écrit » (cochée), la case « Je ne souhaite pas être recontacté·e » (non cochée), et les boutons « Reprendre ma demande » et « Fermer ».
- S'il refuse d'être recontacté ou joint son brouillon, Henri reçoit l'e-mail « Brief interrompu ».
- Si l'onglet est fermé sans fermer la modale, rien de plus ne part : Henri a le contact, mais ni le brouillon ni un éventuel refus.
- Le brouillon reste dans le `localStorage` : le prospect peut reprendre sa demande plus tard.

### Demande de rappel

Depuis l'étape 1, par le bouton « Pas le temps de rédiger ? Rappelez-moi » (téléphone requis). Au clic : écran « C'est noté, je vous rappelle. Je vous rappelle sous 48 h ouvrées au {numéro}. » ; e-mail « Demande de rappel » vers Henri ; brouillon effacé. Elle remplace l'ancien formulaire (nom et numéro saisis à la fermeture de la modale). ([Comment découper le brief…](https://github.com/henritouchard/henritouchard/issues/32))

### Après l'envoi

Écran de confirmation dans la modale : « Merci, c'est envoyé. Je vous réponds sous 48 h ouvrées à {e-mail}. La suite : un échange pour préciser votre besoin. » Le brouillon est effacé. Rien ne part sans un clic du prospect (« Valider », « Rappelez-moi », « Fermer » ou « Envoyer »). ([Comment mesurer les leads…](https://github.com/henritouchard/henritouchard/issues/17), [Comment découper le brief…](https://github.com/henritouchard/henritouchard/issues/32))

### Protections (sans captcha)

Piège à robots sur chaque envoi : coordonnées, brief et demande de rappel (champ caché hors écran, `tabindex="-1"`, `aria-hidden`, nom neutre, `autocomplete="off"` ; tout envoi qui le remplit est rejeté en silence). Limite d'appels par IP, en particulier sur la route qui émet les jetons de dictée. Limites de longueur des textes et de durée de dictée. Plafond de dépenses sur le compte Mistral. ([Quelle architecture…](https://github.com/henritouchard/henritouchard/issues/9), [Comment mesurer les leads…](https://github.com/henritouchard/henritouchard/issues/17), [Voxtral Realtime en français…](https://github.com/henritouchard/henritouchard/issues/11))

## 4. E-mails

Tous envoyés par **Brevo**. Pas de CRM : la boîte mail suffit, avec un libellé Gmail « Lead » posé par un filtre sur l'objet. Tous les e-mails vers Henri ont `Reply-To` = le prospect et portent l'**origine** (`?src=` / UTM, sinon référent ; page d'arrivée) et la date. ([Quelles mentions légales…](https://github.com/henritouchard/henritouchard/issues/18), [Comment mesurer les leads…](https://github.com/henritouchard/henritouchard/issues/17), [Comment découper le brief…](https://github.com/henritouchard/henritouchard/issues/32))

- **« Nouveau contact — {société} — brief en cours »** (vers Henri, au clic sur « Valider ») : coordonnées et préférence de contact.
- **« Brief complété — {société} — besoin cadré / à explorer »** (vers Henri, à l'envoi du brief) : coordonnées et préférence ; orientation ; brief reformulé (en indiquant s'il a été modifié par le prospect) suivi des textes d'origine, sinon les sections SOCIÉTÉ (avec la taille) et BESOIN ; aides utilisées (dictée, reformulation).
- **« Brief interrompu — {société} »** (vers Henri, à la fermeture après « Valider », si refus ou brouillon joint) : signale le refus d'être recontacté le cas échéant ; brouillon s'il est joint.
- **« Demande de rappel — {société} »** (vers Henri) : coordonnées ; pas de brief.
- **Accusé de réception (vers le prospect, après un brief complété)** : court, depuis `contact@henritouchard.fr`, signé Henri : délai (48 h ouvrées), suite (Henri répond personnellement et propose un échange), lien vers les réalisations. **Jamais le texte du brief** (sinon relais de spam vers des tiers). Habillage : le triptyque nuit ou une version allégée. Pas de lien de prise de rendez-vous en V1. ([Comment mesurer les leads…](https://github.com/henritouchard/henritouchard/issues/17))

## 5. Mesure

([Comment mesurer les leads…](https://github.com/henritouchard/henritouchard/issues/17))

- **Umami auto-hébergé** sur le VPS (Node + PostgreSQL) : aucun cookie ni stockage sur l'appareil, IP non conservée, donc ni consentement ni bannière.
- Le site ne mesure que ses trois types de leads : brief, brief interrompu et demande de rappel. Les autres leads (e-mail direct, appel, LinkedIn) ne sont pas suivis.
- **Événements anonymes** (sans contenu ni coordonnées) : `brief_ouvert`, `etape_atteinte` (numéro et nom de l'étape), `coordonnees_envoyees`, `orientation`, `dictee_utilisee`, `reformulation_demandee`, `reformulation_modifiee`, `reformulation_utilisee` (modifiée ou non), `reformulation_refusee`, `brief_envoye`, `brief_quitte` (recontact accepté ou non, brouillon joint ou non), `rappel_demande`. ([Comment découper le brief…](https://github.com/henritouchard/henritouchard/issues/32)) **Objectifs de conversion** : `coordonnees_envoyees`, `brief_envoye`, `rappel_demande`.
- **Origine du lead** : `?src=` ou UTM sur chaque lien diffusé, sinon le référent. Gardée en `sessionStorage` le temps de la visite, écrite dans l'e-mail de lead et jointe à l'événement de conversion.
- **Liens diffusés** : ils visent l'accueil avec `?src=`, sans ouvrir la modale d'office : QR code de la carte de visite `henritouchard.fr/?src=carte`, puis `?src=linkedin`, `?src=malt`, `?src=signature`… (réponse d'Henri du 2026-11-19 sur [Rassembler la spec du site](https://github.com/henritouchard/henritouchard/issues/31))

## 6. Référencement

([Quels réglages techniques de référencement…](https://github.com/henritouchard/henritouchard/issues/12), [Quel référencement technique pour chaque page ?](https://github.com/henritouchard/henritouchard/issues/14) ; détail des réglages : [docs/referencement-technique.md sur la branche de recherche](https://github.com/henritouchard/henritouchard/blob/research/referencement-technique/docs/referencement-technique.md))

### Par page

| Page | `<title>` | H1 | Meta description | Index |
|---|---|---|---|---|
| Accueil | « Automatisation des processus & logiciel sur mesure – Henri Touchard » | le titre « J'optimise vos processus là où ça compte… » (l'intitulé est un paragraphe ; sections en H2) | « Je repère les points de friction de votre entreprise et conçois des logiciels sur mesure, avec ou sans IA, pour libérer votre équipe. Devis gratuit. » | oui |
| Liste | « Expériences et réalisations – Henri Touchard » | « Expériences et réalisations » | la phrase de rappel de l'offre | oui |
| Récit | titre du récit (avec son mot-clé de longue traîne) + « – Henri Touchard » | titre du récit | `description` du frontmatter | oui ; slug = mot-clé |
| À propos | « À propos – Henri Touchard, optimisation opérationnelle » | « Henri Touchard » | — | oui |
| Mentions légales | — | — | — | `noindex`, hors sitemap |

**Mots-clés des premiers récits** (à revoir à la rédaction) : PUM « outil de coordination d'équipes sur mesure » ; Lizee « automatisation des commandes transporteurs » ; SambaÉdu « refonte de logiciel métier » ; GTD à fixer (pas « automatisation des tâches administratives », réservé à un futur récit). ([Quelles réalisations…](https://github.com/henritouchard/henritouchard/issues/7))

### Réglages techniques

- `<title>` et meta description uniques ; titre dans le premier `<h1>` ; canonique absolue et auto-référente.
- **Open Graph** complet sur chaque page, avec **une seule image pour tout le site** (le « triptyque nuit », 1200 × 630, texte tenu dans le carré central) ; seul `og:title` change selon la page. Aucune image par récit. ([Favicon et images Open Graph des récits](https://github.com/henritouchard/henritouchard/issues/23), qui révise [Quel référencement technique…](https://github.com/henritouchard/henritouchard/issues/14))
- **Astro** : `site` renseigné, `build.format: 'directory'`, `trailingSlash: 'always'`. **Caddy** : redirections 301 HTTP → HTTPS, www → apex, ajout de la barre oblique finale.
- **JSON-LD** : `WebSite` sur l'accueil ; `BlogPosting` + `BreadcrumbList` sur les récits (fil d'Ariane **non affiché**, seulement en JSON-LD) ; `ProfilePage` + `Person` (avec `sameAs` : LinkedIn, Malt, GitHub) sur À propos. `Organization` + `logo` facultatif. Jamais `FAQPage`, `HowTo`, `LocalBusiness` ni `ProfessionalService`.
- **Sitemap** : `@astrojs/sitemap` avec `filter` (exclut les mentions légales) et `serialize` ; `lastmod` = `dateModified` réel ; ni `priority` ni `changefreq`.
- **robots.txt** généré par `src/pages/robots.txt.ts` : `User-agent: *`, `Allow: /`, ligne `Sitemap:`. Tous les robots sont autorisés, y compris ceux d'entraînement des IA. `noindex` (jamais `Disallow`) pour masquer une page. Pas de `llms.txt`.
- **Core Web Vitals** : LCP < 2,5 s, INP < 200 ms, CLS < 0,1. Pages statiques, `<Image />`, îlot Svelte du brief chargé à l'ouverture de la modale.
- **Search Console** : propriété de domaine vérifiée par DNS, sitemap soumis, réglage « Search generative AI » laissé activé.

## 7. Légal

Minimum légal, sans juriste ni démarche CNIL supplémentaire. ([Quelles mentions légales et quelle information RGPD sur le site ?](https://github.com/henritouchard/henritouchard/issues/18), à partir de [Quelles obligations légales…](https://github.com/henritouchard/henritouchard/issues/13))

- **Mentions légales** (`/mentions-legales/`) : « Henri Touchard EI » (mention « EI » obligatoire) ; adresse, téléphone, e-mail, SIREN ; directeur de la publication : Henri Touchard ; hébergeur Hostinger (adresse, téléphone), VPS en France ; pas de numéro de TVA (franchise en base) ; « offre réservée aux professionnels ».
- **Confidentialité** (section `#confidentialite` de la même page) :
  - traitements : coordonnées, brief, brief interrompu et demande de rappel (e-mails de lead), dictée et reformulation, journaux du serveur, mesure d'audience, brouillon en `localStorage` (effacé à l'envoi) ;
  - base légale : mesures précontractuelles ; conservation des leads : 3 ans après le dernier contact ; registre des traitements tenu ;
  - sous-traitants : **Mistral** (dictée et reformulation, en France, conservation 30 jours tant que le ZDR n'est pas accordé), **Brevo** (e-mails, société française, données dans l'UE), **Hostinger** (VPS en France). **Aucun transfert hors UE.**
- **Aucune bannière de cookies** : le brouillon est exempté, et Umami se passe de consentement.
- **Côté Mistral** : compte payant, opt-out d'entraînement activé, ZDR demandé, abonnement aux changements de sous-traitants. ([Voxtral Realtime en français…](https://github.com/henritouchard/henritouchard/issues/11))

## 8. Identité visuelle et mouvement

Renvoi à la carte [Charte graphique Henri Touchard](https://github.com/henritouchard/henritouchard/issues/19) (canvas : https://claude.ai/artifact/UWpTaFDEvLb2Xs5t1LUMxy). L'essentiel pour construire le site :

- **Logo** : faisceau en tuile, croisement (7b) : tuile encre nuit aux coins arrondis (rayon 14/64), deux traits blancs qui se croisent puis filent en parallèle, trait corail central terminé par un point placé **au-delà des branches**. Sur les bandes encre, il s'inverse (tuile blanche, traits encre). Géométrie : `mark()` de la branche [`prototype/palette-typo`](https://github.com/henritouchard/henritouchard/tree/prototype/palette-typo/prototypes/palette-typo). ([Quel motif graphique et quel logo définitif ?](https://github.com/henritouchard/henritouchard/issues/20))
- **Couleurs** ([La palette et les typographies…](https://github.com/henritouchard/henritouchard/issues/21), [Quelle identité visuelle…](https://github.com/henritouchard/henritouchard/issues/15)) :
  - encre nuit `#0E1626` ; surface sombre `#172235` ; filets sombres `#263248` / `#37455C` ;
  - fond clair `#FAFAF8`, surfaces `#FFFFFF`, texte secondaire `#3B424B`, texte discret `#5C6570`, filets `#E1E3E6` / `#C3C8CE` ;
  - accent unique : corail `#F0503C` ; corail foncé `#C7362A` pour les liens et le petit texte sur fond clair ;
  - **bandes encre** : navigation (uni), haut de page et appel final (lueur `radial-gradient(ellipse 80% 110% at 100% 0%, #1C2840 0%, #0E1626 65%)`) ;
  - sur l'encre : boutons corail à texte encre, surtitre gris clair `#C4CAD2` ; corail réservé au filet, au point, aux boutons et au très grand texte ;
  - sur fond clair : boutons en encre ; liens, libellés et petit texte d'accent en corail foncé (l'appel final étant sur bande encre, son bouton suit la règle de l'encre : corail à texte encre) ;
  - **interdits** : texte blanc sur corail `#F0503C`, petit texte corail sur fond clair, petit texte corail sur l'encre.
  - Rayons : 4 px (boutons), 8 px (blocs).
- **Typographies** : Space Grotesk 600 (titres), IBM Plex Sans (texte), IBM Plex Mono (libellés, numéros, fiches : `01 / approche`, `friction-01`).
- **Filet** : le seul trait corail terminé par son point ; il accompagne le surtitre, les libellés de section et l'appel final. Pas de motif autonome ni de friction dessinée.
- **Mouvement, « le trait guide »** ([Quels principes de mouvement sur le site ?](https://github.com/henritouchard/henritouchard/issues/22)) : logo tracé au premier chargement (< 1 s) ; chaîne du haut de page construite maillon par maillon (380 ms d'écart) ; filets tracés à l'entrée (700 ms, une fois) ; 4 étapes allumées en séquence (240 ms d'écart) ; survols : flèche des boutons +3 px, soulignement qui s'écarte, point du logo +2 px, cartes soulevées de 3 px avec bordure corail foncé. Jetons : 140 / 220 / 700 ms ; sortie `cubic-bezier(.2,.7,.2,1)`, tracé `cubic-bezier(.65,0,.35,1)` ; IntersectionObserver au seuil 0,3. Règles : uniquement `transform`, `opacity` (et `stroke-dashoffset` pour les tracés) ; titre et texte jamais animés ; aucune boucle ; `prefers-reduced-motion` = état final ; focus visible (contour corail 2 px, décalé de 3 px).
- **Favicon** : 16 et 32 px avec traits renforcés (nuit uni à 16, lueur à 32) ; 48 px et plus en dessin normal ; apple-touch-icon 180 plein bord ; Android maskable 512 réduit à 78 %. ([Favicon et images Open Graph des récits](https://github.com/henritouchard/henritouchard/issues/23))
- **Portrait** : photo existante (kDrive, CV), couleur d'origine, corail seulement autour ; recadrages 4:5 buste et carré serré. ([Quel style pour le portrait photo ?](https://github.com/henritouchard/henritouchard/issues/24))

## 9. Stack et hébergement

([Quelle architecture de pages et quelle stack ?](https://github.com/henritouchard/henritouchard/issues/9), [Voxtral Realtime en français…](https://github.com/henritouchard/henritouchard/issues/11), [Quelles mentions légales…](https://github.com/henritouchard/henritouchard/issues/18), [Comment mesurer les leads…](https://github.com/henritouchard/henritouchard/issues/17))

- **Nouveau dépôt** ; l'ancien CV (dépôt `CV`, SvelteKit) est remplacé.
- **Astro** ; la modale du brief est un composant **Svelte** (îlot chargé à l'ouverture). Récits en Markdown/MDX dans le dépôt, sans CMS.
- **Hébergement** : VPS Hostinger KVM 2 en France. Astro en mode Node (`@astrojs/node` standalone) dans Docker, derrière **Caddy** (HTTPS automatique, redirections, WebSocket si besoin). Déploiement par GitHub Actions à chaque push sur `main`. Umami (+ PostgreSQL) dans ses propres conteneurs. Pas de base de données pour les leads : l'e-mail est la seule trace.
- **Dictée** : Voxtral Realtime (`voxtral-mini-transcribe-realtime-3`), **connexion directe du navigateur** en WebSocket, sans relais audio. Le serveur émet un jeton éphémère `rt_*` (`POST /v1/client/sessions`, ~15 min) ; le navigateur ouvre `wss://…/v1/audio/transcriptions/realtime?model=…` avec le sous-protocole `["realtime", token]`. Audio PCM 16 bits mono 16 kHz en base64 (`input_audio.append`), converti par un AudioWorklet. Endpoint `api.eu.mistral.ai` pour garantir l'UE. Repli si les jetons ne marchent pas : relais de l'audio par le serveur Node.
- **Reformulation** : Mistral Small 4 (`mistral-small-2603`), sortie structurée en quatre rubriques ; Large 4 en repli.
- **E-mails** : Brevo.
- **Coût** : environ 0,017 $ par brief dicté et reformulé (≈ 0,018 $ avec l'endpoint EU).

## 10. À vérifier avant de coder

1. **Voxtral sur l'endpoint EU** (test de 30 min, [Voxtral Realtime en français…](https://github.com/henritouchard/henritouchard/issues/11)) : `models.list` sur `api.eu.mistral.ai` ; jeton `rt_*` avec la v3, sur l'endpoint EU puis le global (la page des jetons est classée « Deprecated » pour la v2) ; temps réel en WebSocket sur l'endpoint EU. Échec → relais de l'audio par le serveur.
2. **Qualité de la dictée en français** sur de vrais enregistrements (2 min, 3 ou 4 briefs) ; régler le délai de transcription au passage (480 ms recommandé par Mistral, 960 ms proposé par la recherche comme compromis).
3. **Mistral en France** : vérifier que le traitement a lieu en France et pas seulement dans l'UE (l'encart dit « en France »). Ne bloque pas la construction.
4. **ZDR chez Mistral** : demande envoyée et réponse obtenue ; s'il est accordé, l'encart et la politique passent à « non conservées ». Ne bloque pas la construction.
