# Intitulés et mots-clés utilisés par les prospects français

Recherche pour l'issue #2 (carte #1). Relevés faits le 17 novembre 2026.

## Question

Quels intitulés et quels mots-clés les startups, scale-ups et PME françaises utilisent-elles pour trouver un développeur indépendant qui fait de l'**optimisation des flux** ? Le résultat doit donner un classement par demande et par niveau de concurrence. Il sert à choisir le titre de l'accueil et les mots-clés des **récits d'expérience**.

## Sources : ce qui a pu être consulté

| Source | Accès | Ce qu'on en tire |
|---|---|---|
| Free-Work, recherche d'offres avec le filtre Freelance | Public, consulté | Nombre d'offres freelance par mot-clé, intitulés réels |
| LinkedIn, pages publiques `fr.linkedin.com/jobs/<terme>-emplois` | Public, consulté | Nombre d'offres (correspondance large) et intitulés. Il s'agit surtout de CDI |
| Malt (recherche, baromètre des tarifs, catégories) | **Bloqué** : HTTP 403 sur toutes les pages en accès automatisé | Seulement les extraits de moteur de recherche des pages Malt, et le rapport PDF public *Malt Trends IA* (2024) |
| Google Trends (France, 12 et 24 mois) | **Bloqué** : HTTP 429 à chaque essai, page rendue en JavaScript | **Aucune donnée.** Aucun chiffre Trends n'est donné ici |
| Volumes de recherche (Google Keyword Planner, Semrush, Ahrefs) | **Connexion requise** | **Aucune donnée.** Aucun volume n'a été trouvé en source publique pour ces termes |

Conséquence : il n'existe aucune mesure de ce que les prospects tapent dans Google. Le classement ci-dessous repose sur la **demande publiée** (offres de missions) et sur l'**offre visible** (profils freelances). Les niveaux sont des **estimations**, signalées comme telles.

## Relevés bruts

### Free-Work, offres freelance (filtre « Freelance », France)

Total des offres freelance du site : **7 817** ([source](https://www.free-work.com/fr/tech-it/jobs?contracts=contractor)).

| Requête | Offres | Intitulés typiques |
|---|---|---|
| `IA` | 990 | Correspondance très large (chef de projet IA, sécurité IA, data…) |
| `fullstack` | 265 | « Développeur Fullstack », « Software Engineer Fullstack .NET / React », « Développeur Golang Fullstack », « Fullstack AI Engineer » |
| `golang` | 178 | La page ne dit pas clairement si le filtre Freelance s'applique à ce compte |
| `automatisation` | 130 | Surtout de l'infrastructure, des réseaux et des tests (NetDevOps, QA, Ansible). Côté métier : « Consultant en automatisation Low-Code », « Consultant IA & Automatisation – Power Automate » |
| `développeur IA` | 52 | « Développeur IA », « Ingénieur développeur IA Full-Stack », « Développeur IA agents / RAG » |
| `automatisation IA` | 35 | Presque aucune offre pertinente (des postes commerciaux d'ESN) |
| `no-code` | 16 | Low-code, Power Platform, ServiceNow |
| `n8n` | 9 | « Ingénieur automatisation / Intégration API », « Agentic AI Engineer » |
| `product engineer` | 5 | « Product Engineer (H/F) », « Développeur Frontend / Product Engineer » |
| `développeur fullstack IA` | 5 | « Développeur Fullstack IA » |
| `CTO` | 3 | « RSI/CTO de transition » (une seule offre pertinente) |
| `forward deployed` | 3 | « Forward Deployed Engineer (FDE) – Ingénieur IA » (une seule) |

URL type : `https://www.free-work.com/fr/tech-it/jobs?query=<terme>&contracts=contractor`. Certaines offres portent aussi l'étiquette CDI. Les donneurs d'ordre sont surtout des ESN et des intermédiaires (missions en régie au TJM), pas des PME en direct.

### LinkedIn, pages publiques d'offres (France)

LinkedIn fait une correspondance large : ses compteurs mélangent les sens (« Product Engineer » inclut « Ingénieur produit » de l'industrie). Ils ne mesurent donc qu'un ordre de grandeur.

| Page | Compteur affiché | Observation |
|---|---|---|
| [product-engineer](https://fr.linkedin.com/jobs/product-engineer-emplois) | « Plus de 9 000 » | En logiciel : des startups et scale-ups (Payfit « Senior AI Product Engineer », Inato, Meteoria, Vocca, The Flex). Il s'agit de CDI. La moitié des offres relèvent de l'ingénierie produit industrielle |
| [forward-deployed-engineer](https://fr.linkedin.com/jobs/forward-deployed-engineer-emplois) | « Plus de 7 000 » | Presque uniquement des éditeurs d'IA et des ESN (OpenAI, Anthropic, Cohere, Devoteam, Alten, Keyrus). Ce sont des CDI. Ce n'est pas un intitulé que cherchent les PME |
| [développeur-freelance](https://fr.linkedin.com/jobs/d%C3%A9veloppeur-freelance-emplois) | « Plus de 6 000 » | 6 des 25 premières offres portent « Freelance » dans l'intitulé, presque toutes via Kicklox. Les intitulés sont « Développeur Full-stack Freelance », « Développeur Front-End Freelance » |
| [développeur-full-stack](https://fr.linkedin.com/jobs/d%C3%A9veloppeur-full-stack-emplois) | « Plus de 5 000 » | Que des CDI, en ESN et en startups (Theodo, Doctolib, Skello) |
| [automatisation-ia](https://fr.linkedin.com/jobs/automatisation-ia-emplois) | « Plus de 10 000 » | Mélange de développeurs IA générative, d'automaticiens industriels (Siemens) et de data scientists. Aucune offre freelance dans les 25 premières |
| [fractional-cto](https://fr.linkedin.com/jobs/fractional-cto-emplois) | 940 | Peu sont réellement fractionnés : « DSI à Temps Partagé », « Mission DSI Freelance à Temps Partagé ». La plupart sont des postes de CTO cofondateur |

Les offres freelance de LinkedIn exigent une connexion pour filtrer par type de contrat. Ce filtre n'a pas été appliqué.

### Malt (extraits indirects)

- La page du baromètre « Développeur Fullstack » indique « Sur Malt, 9484 Développeurs Fullstack freelances sont disponibles pour vos projets ». C'est un extrait de moteur de recherche : la page elle-même est bloquée et n'a pas pu être vérifiée ([page](https://www.malt.fr/t/barometre-tarifs/tech/developpeur-backend/developpeur-fullstack)).
- La page de Malt sur les Product managers annonce « + de 600 Profils Disponibles », et le baromètre mentionne environ 9 235 freelances. Ce sont aussi des extraits ([page](https://www.malt.fr/a/freelance/gestion-de-projets-coaching/product-manager)).
- Aucune catégorie « CTO » ou « Product Engineer » n'apparaît dans le baromètre de Malt, d'après la recherche indirecte.
- **Fractional CTO / CTO à temps partagé** : des profils Malt existent à 800–1 500 €/jour, avec des intitulés comme « Fractional CTO (Temps partagé) » et « CTO à temps partagé » (par exemple [malt.fr/profile/cto](https://www.malt.fr/profile/cto)).
- **Automatisation no-code** : le segment est dense, avec des profils Make, Zapier ou n8n à 330–600 €/jour. Leurs intitulés sont « Consultant Automatisation & No-Code », « Automatisation & Agents IA | n8n · Make · Zapier ». C'est la concurrence directe du mot « automatisation ».
- **Rapport Malt Trends IA, 2024** ([PDF](https://pages.malt.fr/hubfs/NEW%20-%20E-books%20visuals/AI%20Trends%20reports/FR-AI%20TRENDS%20REPORT%20DIGITAL.pdf), données Malt de 2021 à 2024) :
  - Il cite un tech lead : « la plupart des projets d'IA auxquels les entreprises sont confrontées concernent en fait l'automatisation et non la création ».
  - La demande de projets Tech & Data sur Malt a progressé de 70 % entre 2022 et 2024.
  - Il relève que « de nombreuses entreprises confondent à tort les technologies de l'IA et de l'automatisation ».

## Classement (estimation)

La demande est celle des missions et des recherches côté prospect, estimée d'après les offres publiées. La concurrence est celle des freelances qui se présentent sous cet intitulé.

| Rang | Intitulé ou mot-clé | Demande (estimation) | Concurrence (estimation) | Adéquation avec l'offre d'Henri |
|---|---|---|---|---|
| 1 | **Développeur fullstack freelance** / développeur freelance | Forte. C'est l'intitulé n°1 des missions (265 sur Free-Work, des milliers sur LinkedIn) | Très forte : environ 9 500 profils fullstack sur Malt | Moyenne. Le terme est compris de tous, mais il se vend surtout en régie au TJM, donc sans différenciation |
| 2 | **Développeur IA** / intégration IA | Moyenne et en forte hausse (52 offres freelance « développeur IA » sur Free-Work) | Forte et en croissance rapide (l'offre explose selon Malt 2024) | Partielle. L'IA est un levier, pas l'offre |
| 3 | **Automatisation** (des processus, des tâches) | Moyenne, mais le terme est ambigu sur les job boards (infrastructure, QA, industrie) | Forte dans le no-code à bas prix (Make, Zapier, n8n) | Bonne sur le fond, mais le glossaire juge le mot trop étroit pour nommer l'offre |
| 4 | **Product Engineer** | Faible en freelance (5 offres sur Free-Work). Le terme est connu des startups et scale-ups (CDI chez Payfit, Inato…) | Faible | Bonne : regard produit et technique. Peu de recherches, mais il qualifie le profil auprès des startups |
| 5 | **Fractional CTO / CTO à temps partagé** | Faible (3 offres sur Free-Work, une poignée de vraies offres sur LinkedIn) | Moyenne : profils seniors à 800–1 500 €/jour | Faible. C'est du pilotage et du recrutement, pas la construction de systèmes |
| 6 | **Forward Deployed Engineer** | Quasi nulle pour les PME. C'est un intitulé de recrutement des éditeurs d'IA (CDI) | Faible | Faible. Les prospects ne le cherchent pas |
| — | « Intégrateur IA », « consultant automatisation », « automatisation IA » | Faible : 35 offres sur Free-Work pour « automatisation IA », presque toutes hors sujet | Moyenne | Ce sont des variantes des rangs 2 et 3 |
| — | **Optimisation des flux** (terme du glossaire) | **Inconnue**, et probablement très faible en recherche, sans donnée Trends | Inconnue | Excellente sur le fond. À utiliser comme promesse, pas comme mot-clé |

## Constats

1. **Les intitulés que cherchent les job boards ne correspondent pas aux leads visés.** Free-Work et LinkedIn reflètent la régie au TJM via des ESN et des intermédiaires (Kicklox, Free-Work). Une PME qui veut une **mission** au forfait cherche plutôt un problème (« automatiser… », « logiciel sur mesure… ») ou passe par son réseau. Aucune donnée publique ne mesure ces recherches, faute d'accès à Trends et au Keyword Planner.
2. **« Développeur fullstack freelance » est le seul intitulé à forte demande certaine.** Il est saturé et sans différenciation.
3. **L'IA tire la demande, mais elle désigne souvent de l'automatisation** : c'est ce que dit Malt lui-même. Ce constat appuie le positionnement du glossaire, où l'IA est un levier au service de l'optimisation des flux.
4. **« Product Engineer » est un bon qualificatif et un mauvais mot-clé.** Les startups le reconnaissent, la concurrence est faible, mais presque aucune mission freelance ne l'emploie.
5. **« Fractional CTO » et « Forward Deployed Engineer » sont à écarter** comme titre et comme cible SEO pour ce positionnement.

## Recommandation

**Titre de l'accueil.** Associer un intitulé que tout prospect comprend et la promesse d'optimisation des flux, sans miser sur un intitulé à la mode. Par exemple :

> **Développeur fullstack freelance** — je repère les tâches qui font perdre du temps à votre équipe et je construis le système qui les supprime.

« Product engineer » ou « regard business et technique » peut servir de sous-titre. Le mot « IA » vient en appui (« l'IA pour aller plus vite »), jamais en tête.

**Mots-clés SEO pour les récits d'expérience.** Ce sont des propositions : aucun volume n'a été vérifié.

1. développeur fullstack freelance
2. développeur freelance (+ ville, si Henri veut viser le local)
3. automatiser les tâches répétitives / automatisation des processus en PME
4. logiciel sur mesure pour PME / outil interne sur mesure
5. intégrer l'IA dans son entreprise (IA pour PME)
6. développement sur mesure au forfait
7. WMS sur mesure / logistique e-commerce (re-commerce), tiré du récit d'expérience Lizee
8. product engineer freelance (faible volume, faible concurrence, cible startups)

## À vérifier (accès humain requis)

- **Google Trends**, France, 24 mois : comparer « développeur freelance », « développeur fullstack freelance », « automatisation », « automatisation IA », « product engineer », « fractional CTO », « CTO à temps partagé », « développeur IA freelance ».
- **Google Keyword Planner** (un compte Google Ads gratuit suffit) : obtenir les volumes mensuels en France des 8 mots-clés ci-dessus, puis reclasser la liste.
- **Malt connecté** : compter les profils par intitulé (« product engineer », « automatisation », « développeur IA ») et lire les besoins publiés par les entreprises.
