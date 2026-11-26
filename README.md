# The World — Thursday, 26 November 2026

A newspaper-style front page summing up the world news of Thursday
26 November 2026 in one 1024×1024 image, for the make.fun bounty
`news-image-20261126`.

## How it is built

`draw.py` draws the page with PIL (pure vector drawing, no photos):
masthead, a lead story, six news panels and an "In Brief" strip.
`main.py` copies the finished `entry.png` into
`$MAKEFUN_OUTPUT_DIR` (default `/output`), deterministically, and
fails loudly if the copy is incomplete.

Run it:

```sh
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Stories (each first reported on 26 November 2026)

- **Lead — North Korea:** Kim Jong Un inspects nuclear-material
  production and weapons research sites and calls for tactical
  nuclear weapons to be deployed across more domains; KCNA says
  North Korea's status as a nuclear weapons state is "absolutely
  inviolable" (Reuters, CNN, Al Jazeera, 26 Nov).
- **Middle East:** An explosion rocks Sanaa after strikes near the
  airport; the Saudi-led coalition intercepts two Houthi ballistic
  missiles aimed at Riyadh; the Houthis hit Jizan port
  (Al Jazeera live, 26 Nov 00:00 UTC).
- **Europe:** The UK government and the EU publish the texts of two
  Brexit-reset treaties today — food trade and emissions trading —
  alongside the Cutting Costs Bill; the treaties carry a 10-year
  termination clause (BBC, 26 Nov 02:13).
- **Europe:** Euro-area leaders meet today to choose Christine
  Lagarde's successor as ECB president; Lagarde steps down early
  in February 2027 (summit, Thu 26 Nov).
- **USA:** Thanksgiving Day storms batter both coasts — a nor'easter
  brings rain, wind and coastal flooding to the East Coast while
  king tides swamp California (NWS warnings through Thu 26 Nov).
- **Energy:** Oil prices climb on Gulf shipping fears as Iran says
  tankers struck mines in the Strait of Hormuz (Reuters, 26 Nov).
- **Defence:** NATO's secretary general urges Europe to prepare for
  large-scale war (reported Thu 26 Nov).
- **In brief:** Trump says the US could sustain an Iran conflict
  until late January; Ukraine's parliament votes to legalise
  cryptocurrency; France's population is projected to fall by
  3.9 million by 2070 (all reported Thu 26 Nov).

Stories checked and deliberately left out although they lead 26 Nov
front pages: the US tariff plan, the Netanyahu judges'
recommendation, the Savasleyka airbase strike, the Cairo tanker
fire, the Ras Tanura claim, the Sudan drone strikes, the Bangladesh
wage rise, the Ramaphosa court win, the Macy's parade postponement,
the nine children reunited and the Miss Universe crowning were all
first reported on Wednesday 25 November (or earlier); the Norway
oil-licence ruling was 13 November; the Gaza storm warning was
24 November.

## License

MIT — see LICENSE.
