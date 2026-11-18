# Réglages techniques de référencement pour henritouchard.fr

Recherche pour le ticket [#12](https://github.com/henritouchard/henritouchard/issues/12) : quels réglages techniques comptent réellement pour Google et pour les robots des IA en 2026, sur un site Astro (accueil d'offre, récits d'expérience longs en Markdown, À propos).

Sources consultées le 18 novembre 2026. Chaque affirmation renvoie à sa source primaire. Légende :

- **Documenté** : écrit noir sur blanc par l'éditeur (Google, OpenAI, Anthropic, Perplexity, Astro, schema.org…).
- **Mythe** : l'éditeur dit explicitement que ça ne sert pas.
- **Non démontré** : rien dans les sources primaires ne prouve un effet.

## En bref

1. Les bases classiques suffisent, y compris pour les réponses IA de Google : Google écrit qu'« il n'y a aucune exigence supplémentaire pour apparaître dans AI Overviews ou AI Mode » ([AI features](https://developers.google.com/search/docs/appearance/ai-features)) et que l'optimisation pour l'IA générative « reste du SEO » ([guide d'optimisation IA, mai 2026](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)).
2. Les données structurées ne donnent plus que peu de résultats enrichis pour ce type de site : fil d'Ariane (ordinateur seulement), ProfilePage, Organization (logo). FAQ est mort en mai 2026. `ProfessionalService` est déprécié par schema.org.
3. `llms.txt` n'a aucun effet démontré : Google dit qu'il ne l'utilise pas, et aucun éditeur de robot IA ne documente qu'il le lit.
4. Pour les robots IA, il faut distinguer les robots d'**entraînement** (GPTBot, ClaudeBot, Google-Extended) des robots de **recherche** (OAI-SearchBot, Claude-SearchBot, PerplexityBot). Pour un site qui cherche des leads, les robots de recherche doivent rester autorisés.

## 1. Balises de base : title, meta description, H1, Open Graph

### `<title>` (documenté)

Le titre est la première source du lien bleu dans les résultats, mais Google peut aussi utiliser le titre visible, les `<h1>`, `og:title`, les ancres de liens et les données `WebSite` ([title links](https://developers.google.com/search/docs/appearance/title-link)). Bonnes pratiques de Google :

- un titre unique et descriptif sur chaque page, jamais un simple « Accueil » ;
- pas de bourrage de mots-clés ni de texte répété partout ;
- le nom du site en début ou en fin, après un séparateur (`–`, `|`, `:`).

### `<h1>` (documenté)

Google conseille de mettre le titre principal dans le premier `<h1>` visible, et peut prendre le premier titre comme lien s'il y a plusieurs grands titres ([title links](https://developers.google.com/search/docs/appearance/title-link)). En revanche, Google n'exige **ni ordre sémantique des titres ni nombre précis** ([SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)). « Un seul H1 par page » relève de la bonne pratique éditoriale, pas d'une règle de classement.

### Meta description (documenté)

Google construit surtout l'extrait à partir du contenu de la page. Il reprend la meta description quand elle décrit mieux la page ([snippet](https://developers.google.com/search/docs/appearance/snippet)). Elle doit être unique par page, résumer la page plutôt qu'aligner des mots-clés, et peut citer l'auteur ou la date pour un article. La documentation ne la présente nulle part comme un facteur de classement : elle sert le taux de clic.

### Meta keywords (mythe)

« La balise meta keywords n'est pas utilisée par la recherche Google et n'a aucun effet sur l'indexation et le classement » ([special tags](https://developers.google.com/search/docs/crawling-indexing/special-tags), repris dans le [SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)). Google ignore aussi `rel="next"`/`rel="prev"` et l'attribut `lang` : il détecte la langue d'après le texte. Garder `<html lang="fr">` reste utile pour l'accessibilité (lecteurs d'écran), pas pour Google.

### Open Graph (documenté par le protocole, pas par Google)

Open Graph sert l'aperçu des liens partagés sur LinkedIn, Slack ou les messageries, qui sont un canal de trafic majeur ici. Propriétés obligatoires : `og:title`, `og:type`, `og:image` et `og:url`. Pour un récit, on ajoute `og:type=article` avec `article:published_time`, `article:modified_time` et `article:author`. On recommande aussi `og:image:alt`, `og:image:width` et `og:image:height`, ainsi que `og:locale=fr_FR` ([ogp.me](https://ogp.me/)). Google peut lire `og:title` pour le titre et `og:site_name` pour le nom du site ([title links](https://developers.google.com/search/docs/appearance/title-link), [site names](https://developers.google.com/search/docs/appearance/site-names)), mais Open Graph n'est pas un signal de classement documenté.

## 2. URL et canoniques

- **URL lisibles (documenté)** : Google conseille des mots descriptifs dans les URL, qui s'affichent dans le fil d'Ariane. En revanche, un mot-clé dans le domaine ou dans le chemin « a peu d'effet sur le classement » ([SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)). Exemple : `/realisations/automatisation-commandes-transporteurs/`.
- **Canonique (documenté)** : Google veut un `rel="canonical"` **absolu** et **auto-référent** sur chaque page canonique. Il ne faut pas donner des canoniques contradictoires (balise, sitemap, redirections). Il faut rediriger HTTP vers HTTPS et ne lister que des URL HTTPS dans le sitemap ([consolidate duplicate URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)). Ordre de force des signaux : redirection > `rel=canonical` > sitemap.
- **Côté Astro (documenté)** : `site` est « fortement recommandé », car Astro s'en sert pour le sitemap et les URL canoniques. Par défaut, `build.format` vaut `'directory'` (`/about/index.html`) et `trailingSlash` vaut `'ignore'`. La doc conseille d'associer `directory` à `trailingSlash: 'always'` pour éviter les écarts entre le développement et le build. Elle précise aussi que pour les pages pré-rendues, c'est **l'hébergeur** qui gère la barre oblique finale ([configuration reference](https://docs.astro.build/en/reference/configuration-reference/)). Ici l'hébergeur est Caddy : il faut lui faire rediriger en 301 `/x` vers `/x/` (ou l'inverse) et `www` vers l'apex, pour qu'une seule forme réponde.
- **Duplication (mythe)** : il n'existe pas de « pénalité pour contenu dupliqué ». C'est seulement inefficace ([SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)).

## 3. Données structurées JSON-LD

### Ce qui donne encore un résultat enrichi en 2026

La [galerie Google](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) recense 25 fonctionnalités. Google a beaucoup réduit la liste en 2025 et 2026 :

- juin 2025 : sept types retirés (Book Actions, Course Info, ClaimReview, Estimated Salary, Learning Video, Special Announcement, Vehicle Listing) ([blog](https://developers.google.com/search/blog/2025/06/simplifying-search-results)) ;
- janvier 2025 : le fil d'Ariane n'apparaît plus **sur mobile**, seulement sur ordinateur ([blog](https://developers.google.com/search/blog/2025/01/simplifying-breadcrumbs)) ;
- 7 mai 2026 : **la FAQ n'apparaît plus** dans Google ; sa documentation a été retirée le 15 juin 2026 ([changelog](https://developers.google.com/search/updates)).

| Type | Utile ici ? | Ce que ça apporte (documenté) |
|---|---|---|
| `BlogPosting` (variante d'Article) | Oui, sur chaque récit | Aucune propriété obligatoire. Recommandées : `headline`, `image`, `datePublished`, `dateModified`, `author` (type `Person` avec `name` et `url` vers la page À propos). Ça aide Google à afficher le bon titre, la bonne image et la bonne date ; il n'y a pas de rendu enrichi spécifique ([Article](https://developers.google.com/search/docs/appearance/structured-data/article)). |
| `BreadcrumbList` | Oui, sur les récits | Fil d'Ariane dans le résultat, sur ordinateur seulement ([Breadcrumb](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb)). |
| `ProfilePage` + `mainEntity: Person` | Oui, sur À propos | Google cite explicitement « une page "À propos de moi" sur un blog » comme cas valide. La page doit porter sur une seule personne liée au site ([Profile page](https://developers.google.com/search/docs/appearance/structured-data/profile-page)). Le `Person` peut porter `sameAs` (LinkedIn, Malt, GitHub), ce qui aide à identifier l'auteur ([Article](https://developers.google.com/search/docs/appearance/structured-data/article)). |
| `WebSite` (`name`, `url`, `alternateName`) | Oui, sur l'accueil seulement | Principal signal pour le **nom du site** affiché au-dessus du résultat ([site names](https://developers.google.com/search/docs/appearance/site-names)). |
| `Organization` | Facultatif | Pas de propriété obligatoire. Sert au logo dans les résultats et le Knowledge Panel ; on le place sur l'accueil ou sur une page de présentation ([Organization](https://developers.google.com/search/docs/appearance/structured-data/organization)). Pertinent si le logo (piste en cours) doit apparaître. |
| `LocalBusiness` / `ProfessionalService` | **Non** | `LocalBusiness` exige `address` et vise un lieu physique ([Local business](https://developers.google.com/search/docs/appearance/structured-data/local-business)). schema.org indique que `ProfessionalService` est **déprécié** « en raison de la confusion avec Service » ([schema.org](https://schema.org/ProfessionalService)). Un freelance sans local à visiter n'y gagne rien ; mieux vaut un profil d'établissement Google si la visibilité locale compte un jour. |
| `FAQPage`, `HowTo` | **Non** | La FAQ ne s'affiche plus depuis mai 2026 ; HowTo est absent de la galerie. |

Pour les IA, Google est explicite : « Les données structurées ne sont pas requises pour la recherche IA générative, et il n'existe pas de balisage schema.org spécial à ajouter » ([AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)). Les données doivent correspondre au texte visible de la page ([AI features](https://developers.google.com/search/docs/appearance/ai-features)).

**Non démontré** : l'idée que le JSON-LD « aide les LLM à citer le site ». Aucun éditeur (OpenAI, Anthropic, Perplexity) ne le documente.

## 4. Sitemap et robots.txt avec Astro

- **`@astrojs/sitemap` (documenté)** : l'intégration exige `site` et génère `sitemap-index.xml` puis `sitemap-0.xml`. L'option `filter()` exclut des pages, par exemple les mentions légales ou une page de remerciement. `serialize()` règle chaque entrée, et donc `lastmod` page par page. La doc Astro rappelle que **`changefreq` et `priority` sont ignorés par Google**. Elle conseille d'ajouter `<link rel="sitemap" href="/sitemap-index.xml">` et de générer `robots.txt` via `src/pages/robots.txt.ts` pour réutiliser `site` ([Astro sitemap](https://docs.astro.build/en/guides/integrations-guide/sitemap/)).
- **`lastmod` (documenté)** : Google ne l'utilise que s'il est « cohérent et vérifiable », et seulement pour une modification significative de la page ; un changement d'année dans le pied de page ne compte pas ([build sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)). On le tire donc de `dateModified` dans le frontmatter du récit, pas de la date du build.
- **`robots.txt` (documenté)** : il gère l'exploration, pas l'indexation. « Ce n'est pas un mécanisme pour garder une page hors de Google » ; pour ça, il faut `noindex` ([robots intro](https://developers.google.com/search/docs/crawling-indexing/robots/intro)). Les mentions légales passent donc par `noindex` (si on veut les masquer), pas par `Disallow`. Dans ce cas, on ne les met pas non plus dans le sitemap : `noindex` et sitemap se contredisent.

## 5. Robots des IA

| Robot | Éditeur | Rôle | Effet d'un blocage |
|---|---|---|---|
| `Google-Extended` | Google | Jeton de contrôle seulement, sans robot à part : entraînement de Gemini et ancrage (grounding) dans Gemini Apps et Vertex AI | « N'affecte pas l'inclusion dans la recherche Google et n'est pas un signal de classement » ([crawlers Google](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)). N'exclut **pas** des AI Overviews. |
| `GPTBot` | OpenAI | Entraînement | Opt-out d'entraînement seulement ; aucun effet sur ChatGPT Search ([OpenAI bots](https://developers.openai.com/api/docs/bots)). |
| `OAI-SearchBot` | OpenAI | Recherche ChatGPT | Les sites bloqués « ne seront pas affichés dans les réponses de ChatGPT search » ([OpenAI bots](https://developers.openai.com/api/docs/bots)). |
| `ChatGPT-User` | OpenAI | Visite demandée par un utilisateur | robots.txt « peut ne pas s'appliquer » ([OpenAI bots](https://developers.openai.com/api/docs/bots)). |
| `ClaudeBot` | Anthropic | Entraînement | Opt-out d'entraînement ([Anthropic](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)). |
| `Claude-SearchBot` | Anthropic | Indexation pour la recherche | Bloquer « peut réduire la visibilité » dans les résultats ([Anthropic](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)). |
| `Claude-User` | Anthropic | Visite demandée par un utilisateur | Bloquer empêche de récupérer le contenu pour répondre à l'utilisateur ([Anthropic](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)). |
| `PerplexityBot` | Perplexity | Recherche ; « pas utilisé pour entraîner des modèles de fondation » | Perplexity recommande de l'autoriser pour apparaître dans ses résultats ([Perplexity bots](https://docs.perplexity.ai/guides/bots)). |
| `Perplexity-User` | Perplexity | Visite demandée par un utilisateur | « Ignore généralement robots.txt » ([Perplexity bots](https://docs.perplexity.ai/guides/bots)). |

Côté Google, la sortie des AI Overviews et d'AI Mode ne passe pas par robots.txt. Elle passe par le réglage **« Search generative AI »** de Search Console, activé par défaut et ouvert à tous les sites depuis le 31 août 2026. L'exclusion ne touche ni le classement ailleurs dans Search ni l'entraînement, qui dépend de Google-Extended ([aide Search Console](https://support.google.com/webmasters/answer/16908024?hl=en)). Les balises `nosnippet`, `data-nosnippet`, `max-snippet` et `noindex` limitent aussi ce qui est montré ([AI features](https://developers.google.com/search/docs/appearance/ai-features)).

À venir (pas encore en place) : Google prévoit de prendre en charge en 2027 un jeton commun d'opt-out de l'entraînement dans robots.txt, issu du groupe IETF AIPREF ([blog, octobre 2026](https://developers.google.com/search/blog/2026/10/ai-training-control)).

**Pour ce site**, l'objectif est d'être cité et lié par les assistants : il faut laisser passer tous les robots de recherche et les visites à la demande des utilisateurs. Bloquer ou non les robots d'entraînement (GPTBot, ClaudeBot, Google-Extended) est un choix de principe, sans effet documenté sur la visibilité. Pour un site vitrine qui veut être connu, les laisser passer est cohérent. Garder le réglage « Search generative AI » activé (c'est le défaut).

## 6. `llms.txt`

- **Ce que c'est** : une proposition de Jeremy Howard (septembre 2024), qualifiée d'« informelle » et ouverte aux contributions, pensée surtout pour l'usage au moment de l'inférence ([llmstxt.org](https://llmstxt.org/)). Le site note que les labs d'IA **publient** un `llms.txt` pour leur propre documentation développeur, mais n'affirme pas qu'ils en **lisent** sur les sites tiers.
- **Google (documenté, mythe pour la recherche)** : il n'est pas nécessaire de créer « de nouveaux fichiers lisibles par machine, fichiers texte pour l'IA, balisage ou Markdown » ; en créer « ne nuira ni n'aidera à la visibilité » ([AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)). Le changelog du 15 juin 2026 précise qu'on peut le garder pour d'autres services ([updates](https://developers.google.com/search/updates)).
- **Chrome Lighthouse** : un audit « agentic browsing » signale seulement une **erreur serveur** sur `/llms.txt`. Un 404 est marqué « non applicable », car le fichier est « facultatif pour le moment » ([Lighthouse](https://developer.chrome.com/docs/lighthouse/agentic-browsing/llms-txt)).
- **OpenAI, Anthropic, Perplexity** : leurs pages sur les robots ne mentionnent pas `llms.txt` (sources de la section 5).
- **Verdict : non démontré.** Pour un site de quelques pages, le coût est quasi nul. On peut en générer un plus tard, sans en attendre de leads. Ce n'est pas une priorité de la spec.

## 7. Core Web Vitals

Seuils documentés ([Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals)) :

- **LCP** < 2,5 s ;
- **INP** < 200 ms ;
- **CLS** < 0,1.

Google les « recommande vivement » et dit qu'ils sont en phase avec ce que ses systèmes de classement récompensent, **sans en donner le poids**. Ils ne remplacent pas la pertinence du contenu. Un site Astro statique, avec Svelte en îlot limité à la modale du brief, part avec un net avantage. Points de vigilance :

- image principale des récits (LCP) : utiliser `<Image />` d'Astro avec des dimensions fixes ;
- polices web (CLS) ;
- chargement du code de la modale, dictée comprise (INP) : à hydrater à l'ouverture (`client:idle`/`client:visible` ou import dynamique), pas au chargement de la page.

## 8. Google Search Console

- Créer une **propriété de domaine** (`henritouchard.fr`). Elle couvre tous les sous-domaines et protocoles et se vérifie **uniquement par un enregistrement DNS** ([aide](https://support.google.com/webmasters/answer/34592)).
- Soumettre `https://henritouchard.fr/sitemap-index.xml`, puis suivre l'indexation et les rapports de résultats enrichis (fil d'Ariane, ProfilePage).
- Le rapport **« Generative AI performance »** montre les impressions dans AI Overviews et AI Mode par page, appareil et pays. Il n'apparaît que si le site est inclus et a assez d'impressions ([aide](https://support.google.com/webmasters/answer/16984139), [blog juin 2026](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports)). Google conseille de se méfier des outils tiers qui prétendent accéder à des métriques internes ([AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)).

## 9. Prouvé ou mythe : récapitulatif

| Affirmation courante | Statut | Source |
|---|---|---|
| Meta keywords aide le classement | Mythe | [special tags](https://developers.google.com/search/docs/crawling-indexing/special-tags) |
| `priority`/`changefreq` du sitemap comptent | Mythe (ignorés par Google) | [build sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) |
| Pénalité pour contenu dupliqué | Mythe | [SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) |
| Il faut une longueur minimale de texte | Mythe | idem |
| Les titres doivent suivre un ordre H1>H2>H3 strict | Mythe (non exigé) | idem |
| E-E-A-T est un facteur de classement | Mythe (« ce n'en est pas un ») | idem |
| Mot-clé dans le domaine ou l'URL = meilleur classement | Quasi mythe (« peu d'effet ») | idem |
| `llms.txt` améliore la visibilité IA | Non démontré ; mythe pour Google | [AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| Un schema.org spécial est requis pour les AI Overviews | Mythe | idem |
| Découper le contenu en petits morceaux (« chunking ») pour l'IA | Mythe | idem |
| Bloquer Google-Extended retire des AI Overviews | Faux : c'est le réglage Search Console | [crawlers Google](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), [aide](https://support.google.com/webmasters/answer/16908024?hl=en) |
| Bloquer GPTBot retire de ChatGPT Search | Faux : c'est OAI-SearchBot | [OpenAI bots](https://developers.openai.com/api/docs/bots) |
| FAQPage donne des questions dépliables dans Google | Plus depuis mai 2026 | [updates](https://developers.google.com/search/updates) |
| Core Web Vitals comptent | Documenté, poids inconnu | [Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals) |
| `rel=canonical` auto-référent et absolu | Documenté | [canonical](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) |
| Le premier `<h1>` visible sert au lien de titre | Documenté | [title links](https://developers.google.com/search/docs/appearance/title-link) |

## 10. Liste des réglages pour la construction

1. `astro.config.mjs` : `site: 'https://henritouchard.fr'`, `build.format: 'directory'`, `trailingSlash: 'always'`, intégration `@astrojs/sitemap` avec `filter` (exclure ce qui est en `noindex`) et `serialize` (`lastmod` tiré de `dateModified`).
2. Caddy : redirections 301 de HTTP vers HTTPS, de `www` vers l'apex et de l'URL sans barre oblique finale vers celle qui en a une.
3. Composant `<SEO>` dans le layout :
   - `<title>` unique « Titre – Henri Touchard » ;
   - meta description unique ;
   - canonique absolue construite avec `new URL(Astro.url.pathname, Astro.site)` ;
   - Open Graph complet (`og:type=article` sur les récits, `og:image:alt`, `og:locale=fr_FR`) ;
   - `<html lang="fr">` ;
   - `<link rel="sitemap">`.
4. JSON-LD :
   - `WebSite` sur l'accueil (avec `Organization` + `logo` si le logo est retenu) ;
   - `BlogPosting` + `BreadcrumbList` sur chaque récit, avec `author` de type `Person`, `url` vers À propos et `sameAs` ;
   - `ProfilePage` + `Person` sur À propos.
   - Pas de `FAQPage`, `HowTo`, `LocalBusiness` ni `ProfessionalService`.
5. Frontmatter des récits : `title`, `description`, `datePublished`, `dateModified`, `image`, `imageAlt` et un slug lisible portant le mot-clé de longue traîne.
6. `src/pages/robots.txt.ts` :
   - `User-agent: *` + `Allow: /` ;
   - aucun blocage des robots de recherche IA (OAI-SearchBot, Claude-SearchBot, PerplexityBot) ;
   - ligne `Sitemap:` absolue.
7. Mentions légales : `noindex` (facultatif), hors sitemap.
8. Search Console : propriété de domaine vérifiée par DNS, sitemap soumis, réglage « Search generative AI » laissé activé.
9. Performance : `<Image />` avec dimensions, polices auto-hébergées, îlot Svelte du brief chargé à l'ouverture de la modale.
10. `llms.txt` : facultatif, sans effet attendu ; à ne pas compter dans la spec.

## Limites de cette recherche

- Le poids réel de chaque signal (Core Web Vitals, données structurées) n'est jamais publié par Google ; seules les recommandations le sont.
- On ne connaît pas l'effet concret des robots de recherche IA sur le volume de leads ; seul le suivi (rapport Search Console, référents dans les journaux de Caddy) le dira.
- Les déclarations orales attribuées à des employés de Google sur `llms.txt` (Mueller, Illyes) n'ont pas été vérifiées à la source ; seule la documentation écrite est retenue ici.
