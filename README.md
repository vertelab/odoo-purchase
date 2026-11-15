# odoo-purchase — gren 19.0

> **Denna gren är avsiktligt tom.** Modulerna är INTE portade till Odoo 19.
> Grenen finns så att dev-miljöer (`hansolo19`) kan klona den utan att falla,
> men den påstår ingenting om att koden är portad.

## Baseline

| | |
|---|---|
| Källa | `20.0` |
| Moduler | **2** |
| Grenar i repot | `14.0`, `18.0`, `20.0`, `master`, `master10` |

## Moduler

- `purchase_hr_validation`
- `purchase_replenishment_lms`

## Blockerare

**1 externa beroenden saknas** i Odoo 19-kärnan och OCA 19.0:

| Beroende | Behövs av |
|---|---|
| `purchase_tier_validation` | `purchase_hr_validation` |

### Prioritering

Ett beroende som blockerar många moduler ger mest nytta att lösa först:

- `purchase_tier_validation` — frisläpper **1** modul(er)

## Nästa steg

Portering sker på `*-pfile`-maskin med versionsagnostisk kod
(`.p.py` / `.p.xml`). Se `/skill:odoo-pfiles`.
