#!/usr/bin/env python3
"""Builds the Tanya C portfolio deck as 16:9 HTML pages -> PDF via wkhtmltopdf."""

FONT = "file:///usr/share/texmf/fonts/opentype/public/tex-gyre/"

CSS = """
@font-face{font-family:HCN;src:url('__F__texgyreheroscn-bold.otf');font-weight:700}
@font-face{font-family:HCNR;src:url('__F__texgyreheroscn-regular.otf');font-weight:400}
@font-face{font-family:HRS;src:url('__F__texgyreheros-regular.otf');font-weight:400}
@font-face{font-family:HRSB;src:url('__F__texgyreheros-bold.otf');font-weight:700}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#fff}
.slide{width:1280px;height:720px;position:relative;overflow:hidden;
  background:#F5F5F2;color:#111417;font-family:HRS,Arial,sans-serif;page-break-after:always}
.slide.dark{background:#111417;color:#F5F5F2}
.slide.tint{background:#EAEAE4}
.pad{position:absolute;left:78px;right:78px;top:76px}
.mono{font-family:'Liberation Mono',monospace;font-size:11px;letter-spacing:2.1px;
  text-transform:uppercase;color:#6E7479}
.dark .mono{color:#8A9095}
h1{font-family:HCN;font-size:158px;line-height:.84;letter-spacing:-1.5px;text-transform:uppercase}
h2{font-family:HCN;font-size:62px;line-height:.92;letter-spacing:-.4px;text-transform:uppercase}
h3{font-family:HCN;font-size:30px;line-height:1;text-transform:uppercase}
h4{font-family:HCN;font-size:20px;line-height:1.05;text-transform:uppercase}
p{font-size:16.5px;line-height:1.55;color:#33373C}
.dark p{color:#C9CDD1}
.rule{border-top:1.5px solid #111417;height:0}
.dark .rule{border-top-color:#4A4F55}

/* colour control strip */
.strip{position:absolute;left:0;right:0;bottom:0;height:17px}
.strip i{display:block;float:left;width:16.6667%;height:17px}
.folio{position:absolute;left:78px;right:78px;bottom:40px}
.folio .l{float:left}.folio .r{float:right}

/* cover plates */
.plates{position:relative;height:170px}
.plates h1{position:absolute;left:0;top:0;width:1200px}
.pc{color:#00AEEF;opacity:.62}.pm{color:#EC008C;opacity:.62}.py{color:#FFDD00;opacity:.72}

/* artwork slot */
.slot{position:relative;background:#fff;border:1px solid #D3D3CC}
.slot .lbl{position:absolute;left:50%;top:50%;margin:-15px 0 0 -140px;width:280px;
  text-align:center;font-family:'Liberation Mono',monospace;font-size:11px;letter-spacing:2.1px;
  text-transform:uppercase;color:#6E7479;background:#F5F5F2;border:1px solid #D3D3CC;padding:8px 0}
.cnr{position:absolute;width:15px;height:15px}
.cnr b{position:absolute;background:#9AA0A6;display:block}
.cnr .h{width:15px;height:1px;top:0}.cnr .v{width:1px;height:15px;left:0}
.tl{top:11px;left:11px}.tr{top:11px;right:11px}.bl{bottom:11px;left:11px}.br{bottom:11px;right:11px}

/* grids */
.col{float:left}
.clr{clear:both;height:0;font-size:0}
ul{list-style:none}
li{font-size:15.5px;line-height:1.68;color:#33373C}
.dark li{color:#C9CDD1}
li:before{content:"";display:inline-block;width:5px;height:5px;background:#EC008C;
  margin-right:9px;vertical-align:middle}
.tag{display:inline-block;font-family:'Liberation Mono',monospace;font-size:10px;
  letter-spacing:1.6px;text-transform:uppercase;color:#6E7479;border:1px solid #D3D3CC;
  padding:5px 9px;margin:0 5px 5px 0;background:#fff}
.kv{width:100%;border-collapse:collapse}
.kv td{padding:9px 0;border-bottom:1px solid #D3D3CC;font-size:14px;vertical-align:top}
.dark .kv td{border-bottom-color:#3A3E43}
.kv td.k{font-family:'Liberation Mono',monospace;font-size:10.5px;letter-spacing:1.8px;
  text-transform:uppercase;color:#6E7479;width:190px}
.kv td.v{font-family:HRSB;color:#111417}
.dark .kv td.v{color:#F5F5F2}
""".replace("__F__", FONT)

STRIP = ('<div class="strip"><i style="background:#00AEEF"></i><i style="background:#EC008C"></i>'
         '<i style="background:#FFDD00"></i><i style="background:#111417"></i>'
         '<i style="background:#7F8285"></i><i style="background:#D3D3CC"></i></div>')

CORNERS = ('<span class="cnr tl"><b class="h"></b><b class="v"></b></span>'
           '<span class="cnr tr"><b class="h"></b><b class="v" style="right:0;left:auto"></b></span>'
           '<span class="cnr bl"><b class="h" style="bottom:0;top:auto"></b><b class="v"></b></span>'
           '<span class="cnr br"><b class="h" style="bottom:0;top:auto"></b>'
           '<b class="v" style="right:0;left:auto"></b></span>')

TOTAL = 12


def folio(n, label):
    return ('<div class="folio mono"><span class="l">Tanya C — %s</span>'
            '<span class="r">%02d / %02d</span><span class="clr"></span></div>%s'
            % (label, n, TOTAL, STRIP))


def head(no, title, kicker=""):
    k = '<div class="mono" style="margin-bottom:12px">%s</div>' % kicker if kicker else ""
    return ('%s<h2>%s</h2><div class="rule" style="margin:20px 0 30px"></div>' % (k, title))


slides = []

# 01 — cover
slides.append("""
<div class="slide">
  <div class="pad" style="top:118px">
    <div class="plates">
      <h1 class="pc" style="left:-5px;top:-4px">Tanya&nbsp;C</h1>
      <h1 class="pm" style="left:6px;top:3px">Tanya&nbsp;C</h1>
      <h1 class="py" style="left:-2px;top:7px">Tanya&nbsp;C</h1>
      <h1>Tanya&nbsp;C</h1>
    </div>
    <div style="height:34px"></div>
    <div class="rule"></div>
    <div style="margin-top:22px">
      <div class="col" style="width:58%%">
        <h3 style="font-family:HCNR;font-size:34px;letter-spacing:.5px">Graphic Designer
        &nbsp;/&nbsp; Presentation Graphics Specialist</h3>
        <p style="margin-top:16px;max-width:520px">Print, digital and presentation design
        for enterprise brand systems. Portfolio &amp; capability overview.</p>
      </div>
      <div class="col" style="width:42%%">
        <table class="kv">
          <tr><td class="k">Experience</td><td class="v">5+ years</td></tr>
          <tr><td class="k">Current</td><td class="v">Mastercard, New York</td></tr>
          <tr><td class="k">Core tools</td><td class="v">InDesign · Illustrator · PowerPoint</td></tr>
        </table>
      </div>
      <div class="clr"></div>
    </div>
  </div>
  %s
</div>""" % folio(1, "Portfolio"))

# 02 — profile
slides.append("""
<div class="slide tint">
  <div class="pad">
    %s
    <div class="col" style="width:54%%;padding-right:60px">
      <p style="font-size:20px;line-height:1.5;color:#111417">I take dense business
      information — decks, reports, campaign briefs — and turn it into work that holds up
      in front of executives and survives the press check.</p>
      <p style="margin-top:18px">Five years designing high-quality digital, print and
      presentation materials for enterprise organisations in fast-paced corporate
      environments. I work inside existing brand systems rather than around them, and I
      carry a piece from creative brief through to production-ready artwork.</p>
      <p style="margin-top:18px">Day to day that means executive presentations, pitch books,
      brochures, infographics, event graphics and campaign collateral — usually several at
      once, usually to a deadline.</p>
    </div>
    <div class="col" style="width:46%%">
      <h4 style="margin-bottom:14px">How I work</h4>
      <ul>
        <li>Start from the brief and the audience, not the template</li>
        <li>Build systems — masters, grids, styles — so work stays consistent</li>
        <li>Collaborate with creative directors, writers and account teams</li>
        <li>QA every deliverable against brand and editorial standards</li>
        <li>Deliver print-ready and production-accurate files</li>
      </ul>
    </div>
    <div class="clr"></div>
  </div>
  %s
</div>""" % (head(2, "Profile", "01 — Who I am"), folio(2, "Profile")))

# 03 — capabilities
caps = [
    ("Presentation design", ["Executive &amp; marketing decks", "Pitch books, deal books",
                             "Templates and slide masters", "Presentation animation"]),
    ("Print &amp; editorial", ["Brochures, layout design", "Typography, colour theory",
                               "Print-ready artwork", "Production &amp; prepress"]),
    ("Digital &amp; campaign", ["Campaign assets", "Marketing communications",
                                "Promotional collateral", "Event &amp; convention graphics"]),
    ("Information design", ["Infographics", "Data visualisation", "Process &amp; flow diagrams",
                            "Organisational charts"]),
    ("Illustration", ["Vector illustration", "Custom icon systems", "Logos and marks",
                      "Maps and diagrams"]),
    ("Working with teams", ["Creative brief development", "Cross-functional collaboration",
                            "Vendor coordination", "Concurrent deadlines"]),
]
accent = ["#00AEEF", "#EC008C", "#111417"]
blocks = ""
for i, (t, items) in enumerate(caps):
    blocks += ('<div class="col" style="width:33.33%%;padding-right:40px;margin-bottom:34px">'
               '<div style="border-top:3px solid %s;padding-top:12px">'
               '<h4 style="margin-bottom:9px">%s</h4><ul>%s</ul></div></div>'
               % (accent[i % 3], t, "".join("<li>%s</li>" % x for x in items)))
    if i == 2:
        blocks += '<div class="clr"></div>'
slides.append("""
<div class="slide">
  <div class="pad">%s%s<div class="clr"></div></div>
  %s
</div>""" % (head(3, "What I make", "02 — Capabilities"), blocks, folio(3, "Capabilities")))

# 04–09 — work slides
work = [
    ("Executive presentations &amp; pitch books",
     "Slide masters, branded templates and deal books built for people who present them "
     "cold — clear hierarchy, consistent grids, and nothing that breaks when the content "
     "changes the night before.",
     ["PowerPoint", "Slide master", "Templates", "Animation"], "16:9"),
    ("Infographics &amp; data visualisation",
     "Process diagrams, org charts, flow charts and information graphics that make a "
     "complicated argument legible in a single pass.",
     ["Illustrator", "Diagrams", "Charts", "Visual storytelling"], "16:9"),
    ("Brochures &amp; editorial layout",
     "Long-form layout in InDesign: typographic systems, baseline grids and artwork "
     "prepared to production specification.",
     ["InDesign", "Typography", "Print production", "Prepress"], "4:5"),
    ("Brand systems &amp; marketing collateral",
     "Campaign assets that stay inside corporate brand standards across every channel they "
     "land in — digital, print, internal and client-facing.",
     ["Brand identity", "Collateral", "Quality control"], "16:9"),
    ("Icons, logos &amp; vector illustration",
     "Custom icon sets, marks, maps and spot illustration drawn to sit inside an existing "
     "visual language rather than fight it.",
     ["Vector", "Icon sets", "Logo design", "Maps"], "1:1"),
    ("Event, signage &amp; convention graphics",
     "Large-format and environmental pieces — booth graphics, signage and event collateral "
     "built at scale and colour-managed for the printer.",
     ["Large format", "Signage", "Colour management"], "16:9"),
]
SLOT = {"16:9": (709, 399), "4:5": (406, 508), "1:1": (508, 508)}
for i, (title, desc, tags, ratio) in enumerate(work):
    n = i + 4
    slides.append("""
<div class="slide">
  <div class="pad" style="right:0">
    <div class="col" style="width:415px;padding-right:56px">
      <div class="mono" style="margin-bottom:14px">Selected work — %02d of 06</div>
      <h3 style="font-size:38px;line-height:.98">%s</h3>
      <div class="rule" style="margin:20px 0"></div>
      <p>%s</p>
      <div style="margin-top:22px">%s</div>
    </div>
    <div class="col" style="width:709px">
      <div style="width:%dpx;height:%dpx;margin:%dpx auto 0">
        <div class="slot" style="width:100%%;height:100%%">%s<span class="lbl">Artwork slot · %s</span></div>
      </div>
    </div>
    <div class="clr"></div>
  </div>
  %s
</div>""" % (i + 1, title, desc, "".join('<span class="tag">%s</span>' % t for t in tags),
             SLOT[ratio][0], SLOT[ratio][1], (508 - SLOT[ratio][1]) // 2,
             CORNERS, ratio, folio(n, "Selected work")))

# 10 — experience
slides.append("""
<div class="slide tint">
  <div class="pad">
    %s
    <div class="col" style="width:50%%;padding-right:52px">
      <div class="mono">Jun 2024 — Present</div>
      <h3 style="margin:8px 0 4px">Mastercard</h3>
      <div class="mono" style="margin-bottom:14px">Graphic Designer · New York</div>
      <ul>
        <li>Digital and print marketing materials, executive presentations and branded
        communications</li>
        <li>Brochures, presentation templates, infographics, editorial layouts, process
        diagrams, event graphics</li>
        <li>Collaboration with creative directors, writers, account and project managers</li>
        <li>QA against brand and editorial standards before production</li>
        <li>Multiple concurrent projects in a fast-paced Agile environment</li>
      </ul>
    </div>
    <div class="col" style="width:50%%">
      <div class="mono">Mar 2021 — Jul 2023</div>
      <h3 style="margin:8px 0 4px">Enbridge</h3>
      <div class="mono" style="margin-bottom:14px">Graphic Designer</div>
      <ul>
        <li>Print and digital marketing materials, executive presentations, brochures and
        branded assets</li>
        <li>Complex technical information translated into clear visual communication</li>
        <li>Editorial layouts, infographics, illustrations, event graphics, templates</li>
        <li>Print-ready artwork held to colour, brand and production spec</li>
        <li>Support for campaigns, executive meetings, training and corporate events</li>
      </ul>
    </div>
    <div class="clr"></div>
  </div>
  %s
</div>""" % (head(10, "Experience", "04 — Where I've worked"), folio(10, "Experience")))

# 11 — toolbox
tools = [
    ("Adobe", ["InDesign", "Illustrator", "Photoshop", "Acrobat Pro", "Bridge · Creative Cloud"]),
    ("Microsoft", ["PowerPoint (advanced)", "Word · Excel", "Teams · Outlook", "Visio (basic)"]),
    ("Motion &amp; other", ["Adobe Animate", "Premiere Pro (basic)", "After Effects (basic)",
                            "Canva · Figma (basic)"]),
    ("Craft", ["Typography · colour theory", "Layout &amp; grid systems", "Print production",
               "Brand compliance"]),
    ("Delivery", ["Jira · Confluence", "Agile", "Windows 10/11 · macOS", "Vendor coordination"]),
    ("Education", ["M.S. Computer Science, Saint Louis University, MO",
                   "B.Tech Computer Science, Malla Reddy Engineering College"]),
]
tb = ""
for i, (t, items) in enumerate(tools):
    tb += ('<div class="col" style="width:33.33%%;padding-right:40px;margin-bottom:34px">'
           '<div style="border-top:3px solid %s;padding-top:12px">'
           '<h4 style="margin-bottom:9px">%s</h4><ul>%s</ul></div></div>'
           % (accent[i % 3], t, "".join("<li>%s</li>" % x for x in items)))
    if i == 2:
        tb += '<div class="clr"></div>'
slides.append("""
<div class="slide">
  <div class="pad">%s%s<div class="clr"></div></div>
  %s
</div>""" % (head(11, "Toolbox &amp; education", "05 — Tools"), tb, folio(11, "Toolbox")))

# 12 — contact
slides.append("""
<div class="slide dark">
  <div class="pad" style="top:150px">
    <div class="mono" style="margin-bottom:18px">06 — Contact</div>
    <h2 style="font-size:96px;color:#F5F5F2">Let's work</h2>
    <div class="rule" style="margin:34px 0 30px"></div>
    <div class="col" style="width:52%%;padding-right:56px">
      <h3 style="font-size:36px;color:#F5F5F2">hello@example.com</h3>
      <p style="margin-top:12px">Replace with real contact details before sending.</p>
    </div>
    <div class="col" style="width:48%%">
      <table class="kv">
        <tr><td class="k">Based in</td><td class="v">New York, NY</td></tr>
        <tr><td class="k">Phone</td><td class="v">+1 (000) 000-0000</td></tr>
        <tr><td class="k">Portfolio</td><td class="v">tanya-c.example.com</td></tr>
        <tr><td class="k">Available for</td><td class="v">Full-time · Contract · Freelance</td></tr>
      </table>
    </div>
    <div class="clr"></div>
  </div>
  %s
</div>""" % folio(12, "Contact"))

html = ("<!DOCTYPE html><html><head><meta charset='utf-8'><style>%s</style></head><body>%s"
        "</body></html>" % (CSS, "".join(slides)))

with open("/home/claude/deck/deck.html", "w") as fh:
    fh.write(html)
print("slides:", len(slides))
