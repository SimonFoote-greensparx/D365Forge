#!/usr/bin/env python3
"""Emit the website catalogue pages and data from the repository. --check verifies.

Generated: docs/index.html, docs/catalogue.html, docs/templates.html, docs/profile-builder.html, docs/assets/catalogue.json.
Hand-written: docs/assets/site.css. Edit this script, not the HTML.
"""
import html, json
from _common import (departments, skills, templates, sources, load_toml, write_or_check, check_flag, finish, LAYERS, REPO_URL,
                     DISPLAY_NAME, TAGLINE, AUTHORS, MARKETPLACE, CREDIT_LINE, site_page)

check, problems = check_flag(), []
depts, all_skills, tpls = departments(), skills(), templates()
e = html.escape
BLOB = REPO_URL + "/blob/main/"

data = {"departments": [
    {"id": d["id"], "title": d["title"], "layer": d["layer"], "reviewer": d["reviewer"], "lead_role": d["lead_role"],
     "subject_lead": d["subject_lead"], "description": d["description"],
     "skills": [{"name": s["folder"], "title": s["title"], "description": s["description"],
                 "stages": s["meta"].get("stages", ""), "modules": s["meta"].get("modules", ""),
                 "status": s["meta"].get("status", ""), "path": s["path"]}
                for s in all_skills if s["department"] == d["id"]]} for d in depts]}
write_or_check("docs/assets/catalogue.json", json.dumps(data, indent=1, ensure_ascii=False) + "\n", check, problems)


def page(title: str, body: str, active: str) -> str:
    return site_page(title, body, active)


cards = []
for d in data["departments"]:
    skills_html = "".join(
        f'<li data-search="{e((s["name"] + " " + s["title"] + " " + s["description"] + " " + s["modules"]).lower())}">'
        f'<a href="{BLOB}{e(s["path"])}"><code>{e(d["id"])}:{e(s["name"])}</code></a>'
        f'<span class="status {e(s["status"])}">{e(s["status"])}</span><p>{e(s["description"])}</p>'
        f'<p class="meta">Stages: {e(s["stages"])} &middot; Modules: {e(s["modules"])}</p></li>' for s in d["skills"])
    badge = '<span class="badge reviewer">Reviewer-class</span>' if d["reviewer"] else ""
    cards.append(f'<section class="dept layer-{e(d["layer"])}" data-layer="{e(d["layer"])}"><h2>{e(d["title"])} {badge}</h2>'
                 f'<p class="meta">{e(LAYERS[d["layer"]])} &middot; Lead role: {e(d["lead_role"])} &middot; Subject lead: {e(d["subject_lead"])}</p>'
                 f'<p>{e(d["description"])}</p><ul class="skills">{skills_html}</ul></section>')
filters = "".join(f'<button data-filter="{k}">{v}</button>' for k, v in LAYERS.items())
catalogue = f"""<h1>Catalogue</h1>
<p class="lead">{len(depts)} departments and {len(all_skills)} skills. Search by task, product or role, or filter by layer.</p>
<div class="controls"><input id="q" type="search" placeholder="Search skills, e.g. routing, consent, offline, migration" aria-label="Search skills">
<div class="filters"><button data-filter="all" class="on">All</button>{filters}</div><p id="count" aria-live="polite"></p></div>
{''.join(cards)}
<script>
const q=document.getElementById('q'),count=document.getElementById('count');let layer='all';
function apply(){{const t=q.value.trim().toLowerCase();let n=0;
document.querySelectorAll('.dept').forEach(d=>{{let shown=0;const okLayer=layer==='all'||d.dataset.layer===layer;
d.querySelectorAll('li').forEach(li=>{{const ok=okLayer&&(!t||li.dataset.search.includes(t));li.hidden=!ok;if(ok)shown++;}});
d.hidden=shown===0;n+=shown;}});count.textContent=n+' skills shown';}}
q.addEventListener('input',apply);
document.querySelectorAll('.filters button').forEach(b=>b.addEventListener('click',()=>{{
document.querySelectorAll('.filters button').forEach(x=>x.classList.remove('on'));b.classList.add('on');layer=b.dataset.filter;apply();}}));
apply();
</script>"""
write_or_check("docs/catalogue.html", page("Catalogue", catalogue, "Catalogue"), check, problems)

rows = "".join(
    f'<tr><td><a href="{BLOB}{e(t["path"])}">{e(t["front"].get("title", t["path"]))}</a></td><td>{e(t["front"].get("format", ""))}</td>'
    f'<td><code>{e(t["front"].get("owner", ""))}</code></td><td>{e(t["front"].get("tailored_from", ""))}</td>'
    f'<td><span class="status {e(t["front"].get("status", ""))}">{e(t["front"].get("status", ""))}</span></td></tr>' for t in tpls)
tbody = rows or '<tr><td colspan="5">No templates yet.</td></tr>'
tpage = f"""<h1>Template library</h1>
<p class="lead">The documents the <code>project-tailoring:document-pack</code> skill fills from your organisation profile and
exports to Word and Excel. Each links to its source in the repository.</p>
<table class="grid"><thead><tr><th>Template</th><th>Format</th><th>Owner</th><th>Tailored from</th><th>Status</th></tr></thead>
<tbody>{tbody}</tbody></table>
<p>Placeholders such as <code>{{{{organisation.name}}}}</code> and <code>{{{{roles.project-manager}}}}</code> are filled from the profile and the role mapping.
See <a href="{BLOB}templates/README.md">templates/README.md</a> for the placeholder reference.</p>"""
write_or_check("docs/templates.html", page("Templates", tpage, "Templates"), check, problems)

# ---------------------------------------------------------------- home page
srcs = sources()
status_draft = sum(1 for s in all_skills if s["meta"].get("status") == "draft")
layer_blocks = []
for key, label in LAYERS.items():
    chips = "".join(f'<a class="chip" href="{BLOB}plugins/{e(d["id"])}/README.md">{e(d["title"])} <small>{sum(1 for s in all_skills if s["department"] == d["id"])}</small></a>'
                    for d in depts if d["layer"] == key)
    layer_blocks.append(f"<h3>{label}</h3><div class=\"chips\">{chips}</div>")
def author_card(a: dict) -> str:
    photo = a["photo"].removeprefix("docs/")
    bio = "".join(f"<p>{e(p)}</p>" for p in a["bio"])
    return (f'<article class="card author" id="{e(a["slug"])}">'
            f'<div class="author-head"><img src="{e(photo)}" alt="Photo of {e(a["name"])}" width="104" height="104" loading="lazy">'
            f'<div><h3>{e(a["name"])}</h3><p class="headline">{e(a["headline"])}</p>'
            f'<p class="links"><a href="{e(a["url"])}">LinkedIn profile</a></p></div></div>'
            f'{bio}<p class="project-role"><strong>On this project:</strong> {e(a["project_role"])}</p></article>')


author_cards = "".join(author_card(a) for a in AUTHORS)
home = f"""<section class="hero">
<h1>{DISPLAY_NAME}</h1>
<p>{e(TAGLINE)}</p>
<div class="buttons"><a class="btn" href="catalogue.html">Browse the catalogue</a><a class="btn ghost" href="{REPO_URL}">View on GitHub</a><a class="btn ghost" href="profile-builder.html">Build your profile</a></div>
</section>
<div class="notice"><strong>First draft.</strong> All {len(all_skills)} skills are published as drafts ({status_draft} awaiting review) while Robert Peledie reviews them department by department.</div>

<div class="cards">
<div class="card"><div class="stat">{len(depts)}</div><h3>Installable departments</h3><p>Each delivery discipline is a plugin. Install only what your project needs, and the right specialist loads when you ask.</p></div>
<div class="card"><div class="stat">{len(all_skills)}</div><h3>Skills</h3><p>Practitioner judgement for Sales, Marketing, Customer Service and Field Service projects, with SMB and Enterprise notes in every one.</p></div>
<div class="card"><div class="stat">{len(tpls)}</div><h3>Tailored templates</h3><p>Describe your team, goals and estate once to get project roles filled from your team's skills and ready-to-complete documents.</p></div>
<div class="card"><div class="stat">{len(srcs)}</div><h3>Cited sources</h3><p>Microsoft Learn, licensing resources, the ICO and W3C. Skills cite the authority; they never copy it.</p></div>
</div>

<h2>What it is</h2>
<p class="lead">{DISPLAY_NAME} models the team you need to deliver a Microsoft Dynamics 365 Customer Engagement project as an agent organisation.
Four module departments hold the application expertise, ten delivery departments hold the disciplines every CRM project needs, two
reviewer-class departments can block work that breaks design or security standards, and a tailoring department turns your organisation's
profile into a starting pack. It runs in Claude Code, ChatGPT, Codex and Microsoft Copilot Cowork from the same files.</p>

<h2>The organisation</h2>
{''.join(layer_blocks)}
<p><a href="catalogue.html">Search every skill</a></p>

<h2>How it works</h2>
<ol class="steps">
<li><strong>Install the departments you need.</strong> A Field Service rollout with an ERP might install <code>field-service</code>, <code>integration-and-data</code>, <code>solution-architecture</code> and <code>design-authority</code>.</li>
<li><strong>Ask in plain language.</strong> "How should we set up offline profiles for engineers in poor coverage?" loads <code>field-service:mobile-and-offline</code>, which asks the questions that decide the answer before it advises.</li>
<li><strong>Get a tailored pack.</strong> Describe your organisation in a profile; the <code>project-tailoring</code> department recommends an edition, proposes who holds each role from declared skills, shows the gaps, and writes Word and Excel templates for you to complete.</li>
</ol>

<h2>Install</h2>
<p>Claude Code:</p>
<pre><code>/plugin marketplace add SimonFoote-greensparx/{MARKETPLACE}
/plugin install customer-service@{MARKETPLACE}</code></pre>
<p>ChatGPT and Codex: add the repository as a plugin marketplace, or copy the department folders you want into <code>.agents/skills/</code> in your project.
See the <a href="{BLOB}docs/GETTING-STARTED.md">getting-started guide</a> for a starter set for each kind of project.</p>

<h2>Use it in Microsoft Copilot Cowork</h2>
<ol class="steps">
<li><strong>Download the departments you need</strong> from <a href="{REPO_URL}/tree/main/cowork/plugins"><code>cowork/plugins/</code></a>: one plugin archive per department.</li>
<li><strong>Upload them in Cowork:</strong> <em>Customize</em> &gt; <em>Plugins</em> &gt; <em>Upload plugin</em>. Cowork converts each archive into a plugin with its skills, and you can share it with your project team.</li>
<li><strong>Add the suggested custom instructions</strong> from <a href="{BLOB}cowork/custom-instructions.md">cowork/custom-instructions.md</a>, then ask your questions, or attach your organisation profile and ask Cowork to build your project pack as Word and Excel files in your OneDrive.</li>
</ol>
<p>The <a href="{BLOB}docs/COPILOT-COWORK.md">Copilot Cowork guide</a> covers single skills, tailored packs, sharing and organisation-wide rollout.</p>

<h2>Built for real projects, at both scales</h2>
<div class="cards">
<div class="card"><h3>SMB</h3><p>One or two apps, a small partner-led team, one consultant covering several roles, and mostly standard configuration. The skills say what can be simplified and what must not be skipped.</p></div>
<div class="card"><h3>Enterprise</h3><p>Several modules in parallel, a workstream per module, a design authority, automated pipelines and formal SIT and UAT. The skills say what extra roles and controls the scale demands.</p></div>
<div class="card"><h3>Your data stays yours</h3><p>Profiles are built in your browser or kept in a git-ignored folder. Role mapping uses only declared skills and availability; it never ranks people.</p></div>
</div>

<h2 id="authors">Authors</h2>
<div class="authors">{author_cards}</div>

<h2>Use it freely, credit the authors</h2>
<p>{DISPLAY_NAME} is free to use, including commercially and on client projects. The skills, templates and documentation are licensed under
<a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a> and the code under MIT. When you share, republish or adapt them, credit the authors:</p>
<blockquote>{e(CREDIT_LINE)}</blockquote>
<p>Documents you complete for your own project from the templates need no credit. <a href="{BLOB}NOTICE.md">NOTICE.md</a> has the full wording, and
<a href="{BLOB}CITATION.cff">CITATION.cff</a> powers GitHub's <em>Cite this repository</em> button.</p>

<h2>Credits and independence</h2>
<p>The structure follows <a href="https://github.com/cbrock84/headcount">headcount</a> by Chris Brock. All content is original.
{DISPLAY_NAME} is an independent community project, not affiliated with, endorsed by or sponsored by Microsoft. Microsoft, Dynamics 365,
Power Platform, Dataverse and Copilot are trademarks of the Microsoft group of companies. Nothing here is legal, licensing or data-protection advice.</p>
"""
write_or_check("docs/index.html", page("Home", home, "Home"), check, problems)

# ---------------------------------------------------------------- profile builder
vocab = [{"id": v["id"], "d": v["description"]} for v in load_toml("data/skills-vocabulary.toml")["skill"]]
builder = f"""<h1>Profile builder</h1>
<p class="lead">Describe your organisation and download a profile file for the <code>project-tailoring</code> department.
Everything runs in your browser: nothing you type is sent anywhere. Save the file in the <code>input/</code> folder of your copy of the repository.</p>
<form id="f" onsubmit="return false">
<fieldset><legend>Organisation</legend><div class="row">
<div><label for="org_name">Name or alias</label><input type="text" id="org_name" value="Org A"></div>
<div><label for="org_sector">Sector</label><input type="text" id="org_sector"></div>
<div><label for="org_staff">Staff</label><input type="number" id="org_staff" min="1" value="100"></div>
<div><label for="org_entities">Legal entities</label><input type="number" id="org_entities" min="1" value="1"></div>
</div><label for="org_countries">Countries (comma-separated)</label><input type="text" id="org_countries" value="United Kingdom">
<label for="org_reg">Regulatory context (comma-separated)</label><input type="text" id="org_reg" value="UK GDPR, PECR"></fieldset>
<fieldset><legend>Goals</legend>
<label for="g_out">Outcomes (one per line)</label><textarea id="g_out" rows="3"></textarea>
<label for="g_meas">Success measures (one per line)</label><textarea id="g_meas" rows="3"></textarea>
<div class="row"><div><label for="g_live">Target go-live</label><input type="month" id="g_live"></div>
<div><label for="g_budget">Budget band</label><select id="g_budget"><option>not-shared</option><option>under-50k</option><option>50k-250k</option><option>250k-1m</option><option>over-1m</option></select></div></div></fieldset>
<fieldset><legend>Modules</legend><div class="row">
<div><label><input type="checkbox" id="m_sales"> Sales</label><label for="m_sales_u">Users</label><input type="number" id="m_sales_u" min="0" value="0"></div>
<div><label><input type="checkbox" id="m_mkt"> Marketing</label><label for="m_mkt_u">Users</label><input type="number" id="m_mkt_u" min="0" value="0"></div>
<div><label><input type="checkbox" id="m_cs"> Customer Service</label><label for="m_cs_u">Users</label><input type="number" id="m_cs_u" min="0" value="0"></div>
<div><label><input type="checkbox" id="m_fs"> Field Service</label><label for="m_fs_u">Office users</label><input type="number" id="m_fs_u" min="0" value="0"><label for="m_fs_t">Technicians</label><input type="number" id="m_fs_t" min="0" value="0"></div>
</div></fieldset>
<fieldset><legend>Current estate</legend><div class="row">
<div><label for="e_crm">Current CRM</label><input type="text" id="e_crm"></div>
<div><label for="e_erp">ERP</label><input type="text" id="e_erp"></div>
<div><label for="e_tel">Telephony</label><input type="text" id="e_tel"></div>
<div><label for="e_mail">Email and calendar</label><input type="text" id="e_mail" value="Microsoft 365"></div></div>
<label for="e_int">Integrations (one per line: system, direction, frequency)</label><textarea id="e_int" rows="3" placeholder="ERP, both, near-real-time"></textarea>
<label for="e_env">Environments (comma-separated)</label><input type="text" id="e_env" value="development, test, production"></fieldset>
<fieldset><legend>Team</legend>
<p class="meta">Use aliases such as "Analyst A" if you prefer not to use names. Skills come from the shared vocabulary so they match the role catalogue.</p>
<div id="team"></div><button type="button" class="secondary" id="addp">Add a person</button></fieldset>
<fieldset><legend>Constraints and preferences</legend>
<label><input type="checkbox" id="c_partner" checked> An implementation partner is engaged</label>
<label for="c_scope">Partner scope (comma-separated)</label><input type="text" id="c_scope">
<label for="c_risks">Known risks (one per line)</label><textarea id="c_risks" rows="3"></textarea>
<div class="row"><div><label for="p_ed">Edition</label><select id="p_ed"><option>auto</option><option>smb</option><option>enterprise</option></select></div>
<div><label><input type="checkbox" id="p_alias" checked> Use aliases in outputs</label></div></div></fieldset>
<p><button type="button" class="action" id="gen">Generate profile</button> <button type="button" class="secondary" id="dl">Download YAML</button></p>
<label for="yaml">Your profile</label><textarea id="yaml" spellcheck="false"></textarea>
</form>
<script>
const VOCAB={json.dumps(vocab, ensure_ascii=False)};
const LEVELS=["awareness","working","advanced","expert"];
const $=id=>document.getElementById(id);
const list=s=>s.split(",").map(x=>x.trim()).filter(Boolean);
const lines=s=>s.split("\\n").map(x=>x.trim()).filter(Boolean);
const q=s=>JSON.stringify(String(s));
function block(o,ind,key,items){{if(!items.length){{o.push(`${{ind}}${{key}}: []`);return;}}o.push(`${{ind}}${{key}}:`);items.forEach(x=>o.push(`${{ind}}  - ${{x}}`));}}
function skillOptions(){{return VOCAB.map(v=>`<option value="${{v.id}}" title="${{v.d}}">${{v.id}}</option>`).join("");}}
function addSkill(box){{const r=document.createElement("div");r.className="row skill";
r.innerHTML=`<div><select class="sk">${{skillOptions()}}</select></div><div><select class="lv">${{LEVELS.map(l=>`<option>${{l}}</option>`).join("")}}</select></div>`;box.appendChild(r);}}
function addPerson(){{const p=document.createElement("div");p.className="person";
p.innerHTML=`<div class="row"><div><label>Alias</label><input type="text" class="alias" value="Person ${{document.querySelectorAll('.person').length+1}}"></div>
<div><label>Current role</label><input type="text" class="role"></div><div><label>Availability %</label><input type="number" class="avail" min="0" max="100" value="50"></div>
<div><label><input type="checkbox" class="internal" checked> Internal staff</label></div></div><div class="skills"></div>
<button type="button" class="secondary addsk">Add a skill</button> <button type="button" class="secondary rm">Remove person</button>`;
$("team").appendChild(p);addSkill(p.querySelector(".skills"));
p.querySelector(".addsk").onclick=()=>addSkill(p.querySelector(".skills"));p.querySelector(".rm").onclick=()=>p.remove();}}
function mod(id,u,extra){{return `  ${{id}}: {{ in_scope: ${{$(u[0]).checked}}, users: ${{+$(u[1]).value||0}}${{extra||""}} }}`;}}
function gen(){{const o=[];o.push('schema_version: "0.1"');
o.push("organisation:",`  name: ${{q($("org_name").value)}}`,`  sector: ${{q($("org_sector").value)}}`,`  size_staff: ${{+$("org_staff").value||1}}`,
`  countries: [${{list($("org_countries").value).map(q).join(", ")}}]`,`  legal_entities: ${{+$("org_entities").value||1}}`,`  regulatory_context: [${{list($("org_reg").value).map(q).join(", ")}}]`);
o.push("goals:","  outcomes:");(lines($("g_out").value).length?lines($("g_out").value):["Describe an outcome"]).forEach(x=>o.push(`    - ${{q(x)}}`));
block(o,"  ","success_measures",lines($("g_meas").value).map(q));
if($("g_live").value)o.push(`  target_go_live: ${{q($("g_live").value)}}`);o.push(`  budget_band: ${{q($("g_budget").value)}}`);
o.push("modules:",mod("sales",["m_sales","m_sales_u"]),mod("marketing",["m_mkt","m_mkt_u"]),mod("customer_service",["m_cs","m_cs_u"]),
mod("field_service",["m_fs","m_fs_u"],`, technicians: ${{+$("m_fs_t").value||0}}`));
o.push("estate:",`  current_crm: ${{q($("e_crm").value)}}`,`  erp: ${{q($("e_erp").value)}}`,`  telephony: ${{q($("e_tel").value)}}`,`  email_and_calendar: ${{q($("e_mail").value)}}`);
const ints=[];lines($("e_int").value).forEach(l=>{{const [s,d,f]=l.split(",").map(x=>(x||"").trim());let t=`    - {{ system: ${{q(s)}}`;
if(["inbound","outbound","both"].includes(d))t+=`, direction: ${{q(d)}}`;if(["real-time","near-real-time","scheduled","manual"].includes(f))t+=`, frequency: ${{q(f)}}`;ints.push(t+" }}");}});block(o,"  ","integrations",ints);
o.push(`  environments: [${{list($("e_env").value).map(q).join(", ")}}]`);
o.push("team:");const people=document.querySelectorAll(".person");if(!people.length)o.push("  []");
people.forEach(p=>{{o.push(`  - alias: ${{q(p.querySelector(".alias").value)}}`,`    current_role: ${{q(p.querySelector(".role").value)}}`,
`    availability_percent: ${{Math.max(0,Math.min(100,+p.querySelector(".avail").value||0))}}`,`    internal: ${{p.querySelector(".internal").checked}}`,);
block(o,"    ","skills",[...p.querySelectorAll(".skill")].map(s=>`{{ skill: ${{q(s.querySelector(".sk").value)}}, level: ${{q(s.querySelector(".lv").value)}} }}`));}});
o.push("constraints:",`  partner: {{ engaged: ${{$("c_partner").checked}}, scope: [${{list($("c_scope").value).map(q).join(", ")}}] }}`);
block(o,"  ","known_risks",lines($("c_risks").value).map(q));
o.push("preferences:",`  use_aliases: ${{$("p_alias").checked}}`,`  edition: ${{q($("p_ed").value)}}`,'  output_formats: ["docx", "xlsx"]');
$("yaml").value=o.join("\\n")+"\\n";}}
$("addp").onclick=addPerson;$("gen").onclick=gen;
$("dl").onclick=()=>{{if(!$("yaml").value)gen();const b=new Blob([$("yaml").value],{{type:"text/yaml"}});const a=document.createElement("a");
a.href=URL.createObjectURL(b);a.download="our-profile.yaml";a.click();URL.revokeObjectURL(a.href);}};
addPerson();
</script>"""
write_or_check("docs/profile-builder.html", page("Profile builder", builder, "Profile builder"), check, problems)
privacy = f"""<h1>Privacy</h1>
<p class="lead">{DISPLAY_NAME} is a library of skills, templates and documentation. It does not run a service, and it does not collect, store or send any personal or organisation data.</p>
<h2>This website</h2>
<p>The website is a set of static pages hosted on GitHub Pages. It sets no cookies of its own and has no analytics. GitHub, as the host, may log requests as described in GitHub's own privacy statement.</p>
<h2>The profile builder</h2>
<p>The <a href="profile-builder.html">profile builder</a> runs entirely in your browser. Nothing you type is sent anywhere; the profile file is created on your device when you select Download.</p>
<h2>The skills and plugins</h2>
<p>The skills are instructions that run inside the AI assistant you install them in, such as Claude Code, ChatGPT, Codex or Microsoft Copilot Cowork. Any data you share in those conversations is processed under that product's terms and your organisation's agreement with its provider, not by this project. The tailoring skills write organisation profiles and generated documents only to your own storage, never to this repository.</p>
<h2>Contact</h2>
<p>Raise privacy questions with the maintainers listed in <a href="{BLOB}AUTHORS.md">AUTHORS.md</a>.</p>"""
write_or_check("docs/privacy.html", page("Privacy", privacy, "Privacy"), check, problems)
write_or_check("docs/.nojekyll", "", check, problems)
finish("website", problems, len(all_skills))
