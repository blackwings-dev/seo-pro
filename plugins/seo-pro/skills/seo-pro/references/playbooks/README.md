# Playbooks: cross-cutting disciplines

Engine layers (`../engines/`) cover what changes per search engine; vertical layers (`../verticals/`) cover what changes per business model. **Playbooks** cover disciplines every kind of site needs at some point — moving a site, measuring honestly, earning reputation, running SEO as an operation. They expand core practices without renumbering them and use their own ID prefixes.

| File | Discipline | IDs | Expands core | Read when |
|---|---|---|---|---|
| `migrations.md` | Redesigns, CMS/platform changes, domain/URL/HTTPS moves, hosting/CDN/DNS, consolidations, rebrands | M1–M18 | 23, 24, 133–137, 159, **160** | Any change to domain, URLs, CMS, templates, hosting or architecture; "traffic dropped after the redesign" |
| `measurement.md` | Instrumentation, attribution, cohorts, incrementality, experiments, alerts, dashboards | X1–X16 | 40, 107, 108, 116–120, 131, 159 | KPIs, GA4/GSC discrepancies, "did SEO cause this?", tests, alerting, reporting to leadership |
| `reputation.md` | Digital PR, mentions, earned links, reviews, disavow, reputation incidents | R1–R14 | 85–101, 104, 153, 154, 157 | Link building, PR, review programmes, toxic-link panic, reputation crises |
| `programmatic.md` | Template-driven and programmatic pages: data assets, legitimacy test, thresholds, hubs, waves, AI pipelines, pruning | D1–D12 | 26, 45, 54, 121, 155 | Location × service pages, integrations, listings, comparison matrices, glossaries, any large generated page set |
| `governance.md` | Roles and RACI, backlog, prioritisation, editorial and release flow, QA levels Q0–Q4, maintenance, incidents, agencies and AI | G1–G14 | 119, 120, 123, 149, 152, 155, 156 | Teams, agencies, recurring SEO operations, "nothing we recommend gets shipped" |

## How they relate to the rest

- The **plan format** in `SKILL.md` (impact × confidence × reach ÷ effort/risk, confidence column, "what we will NOT do") is the short form of G5 and X8.
- Measurement sections in other layers (A14–A17, L19–L21, E22–E23, P20) apply X1–X16 to their surfaces.
- A migration is a **Q3** change (G7) and is always run with M15's go/no-go.
- Review programmes in `../verticals/local.md` (L9–L11) and R11–R12 are the same rules seen from local SEO and from reputation.

New playbooks get their own file and prefix plus a row here.
