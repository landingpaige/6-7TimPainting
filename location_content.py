# Unique per-city content for the location pages.
#
# This is the source of truth for the differentiated copy on each
# /*-mi (and similar) location page. Regenerate the pages with
# apply_location_content.py after editing this file.
#
# Fields per city:
#   hero          - page-hero intro paragraph (unique per city)
#   feature_para  - "Local Standards" feature-split paragraph
#   svc_interior / svc_exterior / svc_residential / svc_commercial
#                 - the 4 service-card summary sentences
#   local_heading / local_body - one extra section not tied to the
#                 standard 4 services (heading + ~100-150 word paragraph)
#   faqs          - list of (question, answer) tuples, 3 per city,
#                 used for BOTH the visible FAQ section and FAQPage schema

LOCATIONS = {

"berkley-mi": {
  "hero": "Berkley homes and businesses get interior, exterior, residential and commercial painting from a company that shows up on time, protects what's there, and finishes clean. Free written estimates, no subcontractors, and a crew that treats your property like it matters.",
  "feature_para": "Berkley is a compact, walkable community, and that means houses sit close together — overspray, drop cloths, and driveway staging all have to be handled with more care than they would on a larger lot. We tape, mask, and protect neighboring property lines as carefully as we do your own, and we keep the crew's footprint tight so your street stays livable while we work.",
  "svc_interior": "Wall, trim, and ceiling repaints for Berkley's bungalows and updated interiors, with careful masking in tighter floor plans.",
  "svc_exterior": "Exterior repaints suited to Berkley's close-set lots — thorough prep, tidy staging, and coatings built for Michigan winters.",
  "svc_residential": "Full-home repaints and single-room refreshes for Berkley homeowners, scheduled around your household, not ours.",
  "svc_commercial": "Commercial painting for Berkley's small storefronts and office spaces, timed to minimize disruption to business hours.",
  "local_heading": "Painting on a Tighter Lot",
  "local_body": "Close-together homes are common in Berkley, and that changes how a paint job gets run. Ladders, tarps, and paint stations need a plan before the first coat goes on, and exterior work has to account for a neighbor's fence or driveway a few feet away. We walk the property line with you before we start, agree on where equipment will sit, and keep the work area contained so the job doesn't spill onto property that isn't ours to paint. It's a small detail, but it's the kind of thing that determines whether a project feels considerate or intrusive — and it's part of why repeat and referral business matters more to us than any single job.",
  "faqs": [
    ("Do you provide free estimates in Berkley?", "Yes. We'll walk the property with you, talk through the scope, and follow up with a written estimate — no pressure and no obligation."),
    ("Do you paint both interiors and exteriors in Berkley?", "Yes. We handle interior, exterior, residential, and commercial painting throughout Berkley and nearby Royal Oak, Clawson, and Huntington Woods."),
    ("How do you handle overspray and staging on smaller lots?", "We mask and tape thoroughly and keep equipment contained to your property line — something we pay extra attention to in tighter neighborhoods like Berkley."),
  ],
},

"beverly-hills-mi": {
  "hero": "Beverly Hills homeowners hire us for interior and exterior painting that matches the standard already set by the neighborhood — clean lines, careful prep, and a finish that holds up. We're owner-operated, so the person who quotes the job is involved in running it.",
  "feature_para": "Beverly Hills homes tend to have more finish detail than a typical repaint — crown molding, built-ins, multi-color trim schemes — and that raises the bar on prep and cut-in work. We don't rush that part. Careful taping, patient cutting at ceiling and trim lines, and enough coats to get true, even coverage are non-negotiable, whether the room is a formal dining room or a mudroom.",
  "svc_interior": "Detailed interior work for Beverly Hills homes — crown molding, built-ins, and multi-tone trim handled with a steady hand.",
  "svc_exterior": "Exterior painting that respects Beverly Hills curb appeal, with full prep before any color goes on.",
  "svc_residential": "Whole-home repaints and room-by-room updates for Beverly Hills residents, coordinated around your schedule.",
  "svc_commercial": "Commercial and office painting for Beverly Hills-area businesses, scheduled to avoid disrupting operations.",
  "local_heading": "Choosing a Painter in Beverly Hills",
  "local_body": "Homes in this price range and finish level don't leave much room for a rushed paint job to hide. When you're comparing painters, ask who's actually going to be on-site — a company that subcontracts out the work loses a layer of accountability that matters once trim, hardware, and built-ins are involved. Ask how they handle prep on multi-color schemes, how many coats are included, and whether the estimate is written and itemized. We're owner-operated with no subcontractors, which means the person quoting your Beverly Hills project is the same person making sure it's done right.",
  "faqs": [
    ("Do you offer free estimates in Beverly Hills?", "Yes. We provide a free, no-obligation walkthrough and a detailed written estimate for Beverly Hills homes."),
    ("Can you help with color selection?", "Yes. We can talk through finish options and sheen recommendations during your estimate, and provide sample boards if you'd like to test colors before committing."),
    ("Do you paint occupied homes?", "Yes, most of our residential work is done in occupied homes. We protect furniture and flooring and coordinate room-by-room so your household isn't disrupted all at once."),
  ],
},

"bingham-farms-mi": {
  "hero": "Bingham Farms is a small, quiet community, and we bring the same owner-led approach here as we do everywhere else in Metro Detroit — interior, exterior, residential, and commercial painting handled by the same crew from estimate to final walkthrough.",
  "feature_para": "Because Bingham Farms is a smaller village, we don't run it like a high-volume job site — no rotating crews, no subcontractor handoffs. The person who gives your estimate is involved in the work, which means fewer surprises between what's quoted and what's delivered, and a single point of contact if anything needs adjusting mid-project.",
  "svc_interior": "Interior repaints for Bingham Farms homes, from single rooms to full-house refreshes, with clean trim and ceiling lines.",
  "svc_exterior": "Exterior painting prepped and finished for Michigan's freeze-thaw cycle, built to hold up season after season.",
  "svc_residential": "Residential painting for Bingham Farms properties of every size, with an owner on-site throughout the job.",
  "svc_commercial": "Commercial painting for offices and professional spaces near Bingham Farms, scheduled around business hours.",
  "local_heading": "What to Ask Before You Hire a Painter",
  "local_body": "A few questions tend to separate a good painting estimate from a vague one: Is the price written and itemized, or verbal and rough? How many coats are included? Is surface prep — scraping, sanding, caulking, priming — spelled out, or assumed? Who's actually doing the painting — the company you're talking to, or a subcontractor they've hired for the day? For a smaller community like Bingham Farms, we find homeowners appreciate a straightforward answer to all four: written estimate, full prep included, and our own crew on every job, no subcontractors.",
  "faqs": [
    ("Do you offer free estimates near Bingham Farms?", "Yes. We provide free, written estimates for homes and businesses in and around Bingham Farms."),
    ("Are you licensed and insured?", "Yes. Tim MacDonough Painting Company is fully licensed and insured for residential and commercial work throughout the area."),
    ("Do you work with businesses near Bingham Farms?", "Yes. We handle commercial painting for offices and professional buildings nearby, typically scheduled outside of peak business hours."),
  ],
},

"birmingham-mi": {
  "hero": "Birmingham homeowners and business owners have high expectations for finish quality, and that's the standard we hold ourselves to — interior, exterior, residential, and commercial painting with careful prep and an owner involved in every job, not just the estimate.",
  "feature_para": "Birmingham has a mix of older homes with original trim and plaster, and newer builds and renovations with more contemporary finishes. Both require different prep — older surfaces often need more scraping, sanding, and priming before paint goes on, while newer drywall and trim need careful masking to get sharp lines. We treat each on its own terms rather than running every job through the same process.",
  "svc_interior": "Interior painting for Birmingham homes old and new — plaster and original trim get the extra prep they need.",
  "svc_exterior": "Exterior painting for Birmingham properties, with surface prep suited to the age and material of your home.",
  "svc_residential": "Residential repaints across Birmingham, from downtown-adjacent homes to larger properties on quieter streets.",
  "svc_commercial": "Commercial painting for Birmingham's offices, retail spaces, and professional buildings, minimizing disruption to your business.",
  "local_heading": "Older Homes Need a Different Kind of Prep",
  "local_body": "A lot of Birmingham's housing stock is older than the Metro Detroit average, and older surfaces — plaster walls, original wood trim, multiple layers of prior paint — don't behave the same way fresh drywall does. Paint doesn't adhere well over chalky or peeling layers, and skipping the scrape-and-prime step just means the new coat fails faster. We budget real time for prep on older homes rather than treating it as a formality, because the finish only holds up as well as what's underneath it.",
  "faqs": [
    ("Do you offer free estimates in Birmingham?", "Yes. We'll walk your property and provide a free, written estimate with the scope of prep and painting spelled out."),
    ("Can you match or update the trim and color scheme on an older home?", "Yes. We can work with existing color schemes or help you update them, and we're comfortable working around original trim and plaster."),
    ("Do you paint both interiors and exteriors in Birmingham?", "Yes. We handle interior, exterior, residential, and commercial painting throughout Birmingham and nearby Bloomfield Hills, Beverly Hills, and Franklin."),
  ],
},

"bloomfield-hills-mi": {
  "hero": "Bloomfield Hills properties often carry more architectural detail and higher finish expectations than a standard repaint, and that's exactly the kind of work we're built for — owner-led, no subcontractors, and a process built around getting it right the first time.",
  "feature_para": "Estate-scale homes in Bloomfield Hills often mean more surface area, more trim detail, and more coordination — multiple rooms or an entire exterior painted on a timeline that doesn't leave the property looking half-finished for weeks. We plan the sequence of a large job in advance, so work moves room to room or side to side with a clear schedule, not an open-ended one.",
  "svc_interior": "Interior painting for Bloomfield Hills homes with detailed trim, coffered ceilings, and multi-room color coordination.",
  "svc_exterior": "Exterior painting for larger Bloomfield Hills properties, planned and staged to keep the project moving on schedule.",
  "svc_residential": "Estate-level residential painting for Bloomfield Hills, with an owner overseeing the project from start to finish.",
  "svc_commercial": "Commercial and professional-office painting near Bloomfield Hills, handled with the same finish standard as our residential work.",
  "local_heading": "Planning a Larger Painting Project",
  "local_body": "Bigger homes and estate properties benefit from a plan before the first drop cloth goes down — which rooms or exterior sides get painted in what order, how long each phase takes, and how the household or business keeps functioning while work is underway. We walk through that sequence with you at the estimate stage, not after the job has started, so a Bloomfield Hills project has a clear beginning, middle, and end rather than dragging on room by room without a schedule.",
  "faqs": [
    ("Do you offer free estimates for larger properties in Bloomfield Hills?", "Yes. For larger or multi-phase projects, we walk the full property and provide a detailed written estimate that breaks out scope and sequencing."),
    ("Can you coordinate colors across multiple rooms or the full exterior?", "Yes. We can help plan a cohesive color scheme across rooms or an entire exterior, and provide samples before committing to a full repaint."),
    ("Do you paint occupied homes in Bloomfield Hills?", "Yes. Most estate-level work is done in phases while the home stays occupied, with furniture and flooring protected room by room."),
  ],
},

"clawson-mi": {
  "hero": "Clawson is a tight-knit community of well-kept older homes, and we approach every project here the same way — careful prep, an owner on-site, and a finish that holds up to real use, not just how it looks on move-out day.",
  "feature_para": "Clawson's housing stock skews older, with a lot of original trim, plaster, and multiple past paint layers. That means surface prep does more of the work than the paint itself — scraping loose material, sanding rough edges, and priming bare spots before color goes on. We don't shortcut that step, because a rushed prep job is the most common reason a repaint fails early.",
  "svc_interior": "Interior repaints for Clawson's older homes, with extra attention to trim and plaster surfaces that need proper prep.",
  "svc_exterior": "Exterior painting built to last through Michigan winters, with full scraping, sanding, and priming before any topcoat.",
  "svc_residential": "Residential painting for Clawson homeowners updating a room, a full interior, or the whole exterior.",
  "svc_commercial": "Commercial painting for Clawson's small businesses and offices, scheduled around your operating hours.",
  "local_heading": "When Is It Time to Repaint?",
  "local_body": "Interior walls usually show their age before anyone thinks to repaint them — scuffed corners, dulled sheen, or a color that no longer matches how a room is used. Exteriors give clearer warning signs: chalking that rubs off on your hand, cracked or peeling paint, or bare wood exposed at trim and joints. In a community like Clawson with a lot of older housing stock, we'd rather catch peeling or moisture damage early than wait until it's spread to the substrate underneath, since that turns a repaint into a repair.",
  "faqs": [
    ("Do you offer free estimates in Clawson?", "Yes. We provide a free walkthrough and written estimate for Clawson homes and businesses."),
    ("What surfaces can you paint?", "Interior walls, trim, ceilings, and cabinets, along with exterior siding, trim, doors, shutters, and porches — including older plaster and original wood trim common in Clawson."),
    ("Do you paint both interior and exterior properties in Clawson?", "Yes. We handle interior, exterior, residential, and commercial painting throughout Clawson and nearby Royal Oak, Berkley, and Troy."),
  ],
},

"clinton-township-mi": {
  "hero": "Clinton Township covers a lot of ground, and we serve homes and businesses across it with the same standard — interior, exterior, residential, and commercial painting, quoted honestly and finished by the crew that gave you the estimate.",
  "feature_para": "A township this size means a wide range of property types — subdivisions of similar-era homes, standalone properties on larger lots, and commercial buildings along the main corridors. We don't run a one-size-fits-all process; a subdivision repaint gets planned differently than a standalone property with more exterior square footage, and we scope each job on its own before quoting it.",
  "svc_interior": "Interior painting for Clinton Township homes across subdivisions and standalone properties alike.",
  "svc_exterior": "Exterior painting suited to Clinton Township's mix of home styles, with prep matched to each property's condition.",
  "svc_residential": "Residential repaints for Clinton Township homeowners, scheduled to fit around your household.",
  "svc_commercial": "Commercial painting along Clinton Township's business corridors, timed to minimize downtime for your operation.",
  "local_heading": "Planning Your Painting Project",
  "local_body": "The most useful thing a homeowner can do before painters arrive is decide on scope and priorities up front — is this a single room, a full interior, or the exterior too? Are there specific problem areas, like a water-stained ceiling or peeling trim, that need to be flagged before the estimate? We walk Clinton Township properties room by room (or side by side, for exteriors) during the estimate so nothing gets missed, and so the written proposal reflects the actual condition of your property, not a rough guess.",
  "faqs": [
    ("Do you provide free estimates in Clinton Township?", "Yes. We provide a free walkthrough and written estimate for homes and businesses throughout Clinton Township."),
    ("How should I prepare before painters arrive?", "Clearing furniture away from walls and removing wall decor helps, but we handle the heavier protection — drop cloths, taping, and covering fixtures — as part of the job."),
    ("Do you work with businesses in Clinton Township?", "Yes. We handle commercial painting for offices, retail, and professional spaces along Clinton Township's business corridors."),
  ],
},

"franklin-mi": {
  "hero": "Franklin is a small, wooded community, and homes here often call for the same careful, unhurried approach we'd bring to a much larger estate — interior and exterior painting with real attention to detail, done by an owner-operated crew.",
  "feature_para": "Wooded lots like the ones common in Franklin mean more shade, more moisture retention on siding and trim, and often more organic debris — leaves, pollen, sap — that needs to be cleaned off before paint will adhere properly. We factor that into exterior prep here specifically, with a more thorough wash and dry-time buffer than we'd use on an open, sun-exposed lot.",
  "svc_interior": "Interior painting for Franklin homes, with careful trim work and color consultation for wood-heavy interiors.",
  "svc_exterior": "Exterior painting adjusted for wooded, shaded lots — extra cleaning and dry time before coatings go on.",
  "svc_residential": "Residential painting for Franklin properties, handled with the same care whether it's one room or the whole house.",
  "svc_commercial": "Commercial painting for small businesses and offices near Franklin, scheduled around your hours.",
  "local_heading": "Exterior Painting Considerations in Southeast Michigan",
  "local_body": "Southeast Michigan's freeze-thaw winters and humid summers are hard on exterior paint regardless of neighborhood — moisture gets into hairline cracks, freezes, and expands them further, while UV exposure fades and chalks lower-quality coatings over a few seasons. Spring and fall tend to offer the most reliable temperature and humidity windows for exterior work, though we plan around each property's specific exposure — shade from mature trees, as is common on wooded lots like many in Franklin, changes how long surfaces take to dry between coats.",
  "faqs": [
    ("Do you offer free estimates in Franklin?", "Yes. We provide a free walkthrough and written estimate for Franklin homes."),
    ("When is the best time to schedule exterior painting in Michigan?", "Spring and fall generally offer the most consistent temperature and humidity for exterior work, though we can often accommodate summer scheduling as well."),
    ("Do you paint homes on wooded or shaded lots?", "Yes. Shaded, wooded lots need extra drying time and cleaning before painting, which we factor into scheduling for properties like those common in Franklin."),
  ],
},

"grosse-pointe-farms-mi": {
  "hero": "Grosse Pointe Farms homes range from classic older properties to updated family houses, and we bring the same owner-led painting process to every one — interior, exterior, residential, and commercial work with an owner on-site, not just a crew.",
  "feature_para": "The Grosse Pointes sit along Lake St. Clair, and homes closer to the water deal with more humidity and moisture exposure than inland properties. Older Grosse Pointe Farms homes also tend to carry decades of prior paint layers. Between the two, we lean on more thorough prep — scraping, sanding, priming — and moisture-conscious coatings rather than treating every exterior the same.",
  "svc_interior": "Interior painting for Grosse Pointe Farms homes, from original trim and plaster to updated, renovated interiors.",
  "svc_exterior": "Exterior painting with moisture-conscious prep and coatings, suited to Grosse Pointe Farms' proximity to the lake.",
  "svc_residential": "Residential repaints for Grosse Pointe Farms properties of every era, handled with an owner on-site throughout.",
  "svc_commercial": "Commercial painting for offices and professional spaces in and around Grosse Pointe Farms.",
  "local_heading": "Painting Near the Water",
  "local_body": "Homes near Lake St. Clair — which includes much of Grosse Pointe Farms — deal with more ambient humidity than inland Metro Detroit properties, and that affects how paint cures and how long it lasts. We give lakeside exteriors more dry time between coats and lean on coatings designed to resist moisture intrusion, particularly around window trim, soffits, and other spots where water tends to collect. It's a small adjustment, but skipping it is one of the more common reasons exterior paint fails early on properties near the water.",
  "faqs": [
    ("Do you offer free estimates in Grosse Pointe Farms?", "Yes. We provide a free walkthrough and written estimate for homes throughout Grosse Pointe Farms."),
    ("Do you use different products for homes near the lake?", "Yes, where it's warranted. Homes closer to Lake St. Clair benefit from more moisture-resistant coatings and extra prep time, which we account for during the estimate."),
    ("Are you licensed and insured in Grosse Pointe Farms?", "Yes. Tim MacDonough Painting Company is fully licensed and insured for all painting work in Grosse Pointe Farms and the surrounding Grosse Pointe communities."),
  ],
},

"grosse-pointe-mi": {
  "hero": "The City of Grosse Pointe has some of the oldest housing stock in the Grosse Pointe communities, and older homes deserve a painter who won't rush the prep. We handle interior, exterior, residential, and commercial painting with an owner involved from estimate to final coat.",
  "feature_para": "A lot of Grosse Pointe's homes were built well before modern paint chemistry existed, which means original plaster, older trim profiles, and multiple layers of prior paint are the norm rather than the exception. That changes the prep timeline — more scraping, more sanding, more priming — and we build that into the estimate up front rather than discovering it (and adding cost) mid-project.",
  "svc_interior": "Interior painting for Grosse Pointe's older homes, with real prep time for plaster and original trim.",
  "svc_exterior": "Exterior painting with the extra scraping and priming that older Grosse Pointe housing stock typically needs.",
  "svc_residential": "Residential repaints for Grosse Pointe homeowners, whether it's a single room or the full property.",
  "svc_commercial": "Commercial painting for Grosse Pointe's offices and small businesses.",
  "local_heading": "What Older Homes Need Before Repainting",
  "local_body": "A home with decades of paint history usually needs more prep time than a newer build, not more paint. Loose or peeling layers have to come off before new paint goes on, bare wood needs priming, and plaster walls sometimes need patching before they'll take a coat evenly. Skipping straight to color is tempting because it's the visible part of the job, but on a lot of Grosse Pointe's older homes, the prep work is what actually determines how long the new paint holds up.",
  "faqs": [
    ("Do you offer free estimates in Grosse Pointe?", "Yes. We provide a free walkthrough and written estimate, including an honest look at what prep an older home will need."),
    ("Can you match existing trim or wall colors?", "Yes. We can color-match existing paint or help you choose something new during the estimate."),
    ("Do you paint both interior and exterior properties in Grosse Pointe?", "Yes. We handle interior, exterior, residential, and commercial painting throughout Grosse Pointe and the neighboring Grosse Pointe communities."),
  ],
},

"grosse-pointe-shores-mi": {
  "hero": "Grosse Pointe Shores sits directly on Lake St. Clair, and homes here — many of them larger, older, or custom-built — call for a painter who treats prep and moisture protection as seriously as the finish coat. We handle interior, exterior, residential, and commercial painting with an owner on every job.",
  "feature_para": "Being right on the water changes what an exterior paint job has to withstand — more humidity, more reflected light off the lake, and often more exposure on the water-facing side of the home than the street-facing side. We plan for that asymmetry rather than treating all four sides of a Grosse Pointe Shores home the same, and we use coatings suited to near-water exposure.",
  "svc_interior": "Interior painting for Grosse Pointe Shores homes, including larger and custom-built properties.",
  "svc_exterior": "Exterior painting built for lakefront exposure — moisture-resistant coatings and extra prep on water-facing sides.",
  "svc_residential": "Residential painting for Grosse Pointe Shores estates and family homes alike.",
  "svc_commercial": "Commercial painting for professional and office spaces in and around Grosse Pointe Shores.",
  "local_heading": "Painting a Lakefront Property",
  "local_body": "A water-facing exterior wears differently than the rest of the house — more reflected sun, more humidity, and often more direct wind exposure off the lake. On a lakefront property in Grosse Pointe Shores, we typically plan for that side to need a more moisture-resistant coating and a closer eye during the walkthrough for early signs of wear, like chalking or hairline cracking near trim. It's worth budgeting slightly more attention there than you would on an inland home, since that side of the house is doing more work.",
  "faqs": [
    ("Do you paint lakefront homes in Grosse Pointe Shores?", "Yes. We regularly work on lakefront and near-water properties and use moisture-resistant coatings and extra prep suited to that exposure."),
    ("Do you offer free estimates in Grosse Pointe Shores?", "Yes. We provide a free walkthrough and written estimate for homes throughout Grosse Pointe Shores."),
    ("Are you licensed and insured for larger or custom homes?", "Yes. Tim MacDonough Painting Company is fully licensed and insured, and we're comfortable scoping larger or custom-built properties."),
  ],
},

"grosse-pointe-woods-mi": {
  "hero": "Grosse Pointe Woods is a family-oriented community with a mix of established and updated homes, and we handle interior, exterior, residential, and commercial painting here with the same owner-led standard we bring to every Grosse Pointe project.",
  "feature_para": "A lot of Grosse Pointe Woods homes have been updated or renovated over the years, which sometimes means mismatched trim colors, patched drywall from remodeling, or transitions between original and newer surfaces. We look for that during the walkthrough — patched areas often absorb paint differently than surrounding drywall — so the estimate accounts for it and the finish reads as one consistent surface, not a patchwork.",
  "svc_interior": "Interior painting for Grosse Pointe Woods homes, with attention to patched or renovated areas that need extra prep.",
  "svc_exterior": "Exterior painting for Grosse Pointe Woods properties, prepped and finished for Michigan's seasonal weather swings.",
  "svc_residential": "Residential repaints for Grosse Pointe Woods families, scheduled around school and household routines.",
  "svc_commercial": "Commercial painting for Grosse Pointe Woods businesses and professional offices.",
  "local_heading": "Painting After a Renovation",
  "local_body": "If part of a room or a home's exterior has been patched, replaced, or remodeled at some point, that section often takes paint differently than the surrounding original surface — new drywall is more porous, patched plaster can flash through a finish coat unevenly, and mismatched primer coverage shows up under certain lighting. Before painting a renovated area in a Grosse Pointe Woods home, we prime it separately so the final coat goes on over a consistent surface, rather than trying to cover the difference with extra paint alone.",
  "faqs": [
    ("Do you offer free estimates in Grosse Pointe Woods?", "Yes. We provide a free walkthrough and written estimate for homes throughout Grosse Pointe Woods."),
    ("Can you paint over recently patched or renovated areas?", "Yes. We prime patched or renovated sections separately so they blend with the rest of the surface instead of flashing through the topcoat."),
    ("Do you work with businesses in Grosse Pointe Woods?", "Yes. We handle commercial painting for offices and professional spaces throughout Grosse Pointe Woods."),
  ],
},

"huntington-woods-mi": {
  "hero": "Huntington Woods is a small, close-knit city, and homeowners here tend to want a painter they can actually reach — not a call center. We handle interior, exterior, residential, and commercial painting with the owner involved from your first call through the final walkthrough.",
  "feature_para": "Being a smaller city, Huntington Woods doesn't have the anonymity of a larger suburb — word travels between neighbors, and a rushed or sloppy paint job doesn't stay quiet for long. We treat every project here knowing that, with the same prep standards and cleanup we'd want if it were our own street.",
  "svc_interior": "Interior painting for Huntington Woods homes, finished cleanly with attention to trim and ceiling lines.",
  "svc_exterior": "Exterior painting for Huntington Woods properties, prepped thoroughly and finished for lasting curb appeal.",
  "svc_residential": "Residential repaints for Huntington Woods families, from single rooms to full-home projects.",
  "svc_commercial": "Commercial painting for small businesses and offices in and around Huntington Woods.",
  "local_heading": "What Neighbors Notice",
  "local_body": "In a smaller community like Huntington Woods, a paint job doesn't just affect the homeowner — it's visible to everyone on the street for years afterward. That's part of why we treat cleanup and site care as seriously as the painting itself: contained equipment, protected landscaping, and a driveway and yard left the way we found them. A good finish matters, but so does not leaving a mess behind for the neighbors to notice.",
  "faqs": [
    ("Do you offer free estimates in Huntington Woods?", "Yes. We provide a free walkthrough and written estimate for Huntington Woods homes and businesses."),
    ("How do you handle cleanup after a project?", "We remove equipment, protect landscaping throughout the job, and leave the property as clean as we found it — no leftover materials or debris."),
    ("Do you paint both interior and exterior properties in Huntington Woods?", "Yes. We handle interior, exterior, residential, and commercial painting throughout Huntington Woods and nearby Royal Oak, Berkley, and Pleasant Ridge."),
  ],
},

"lathrup-village-mi": {
  "hero": "Lathrup Village is a small city with a distinct residential character, and we bring the same careful, owner-led process here that we do on any Metro Detroit project — interior, exterior, residential, and commercial painting with real attention to prep and finish.",
  "feature_para": "Smaller communities like Lathrup Village often have a mix of home ages and styles within just a few blocks, which means we can't assume one prep approach fits every job here. We scope each property individually during the estimate — checking trim condition, prior paint layers, and any problem areas — rather than quoting from a standard template.",
  "svc_interior": "Interior painting for Lathrup Village homes, scoped individually rather than treated as a one-size-fits-all job.",
  "svc_exterior": "Exterior painting for Lathrup Village properties, with prep matched to each home's age and condition.",
  "svc_residential": "Residential repaints for Lathrup Village homeowners, from single-room updates to full-property projects.",
  "svc_commercial": "Commercial painting for offices and professional spaces near Lathrup Village.",
  "local_heading": "Preparing Your Home for Painting",
  "local_body": "A little prep on your end can make a project run smoother: clearing small items and wall decor from the rooms being painted, moving furniture away from walls where possible, and flagging any areas you're specifically concerned about — a water stain, peeling trim, a crack in the plaster. We handle the heavier protective work ourselves, including drop cloths, taping, and covering fixtures and flooring, but a little advance notice on trouble spots helps us plan the estimate accurately for your Lathrup Village home.",
  "faqs": [
    ("Do you offer free estimates in Lathrup Village?", "Yes. We provide a free walkthrough and written estimate for Lathrup Village homes and businesses."),
    ("How should I prepare before painters arrive?", "Clearing wall decor and small items from the room helps, and flagging specific problem areas in advance lets us plan for them at the estimate stage."),
    ("Do you paint occupied homes in Lathrup Village?", "Yes. Most of our residential work is done in occupied homes, with furniture and flooring protected throughout the project."),
  ],
},

"macomb-township-mi": {
  "hero": "Macomb Township has grown quickly, and that means a wide mix of home ages — newer construction alongside more established properties. We handle interior, exterior, residential, and commercial painting for both, with the same owner-led standard on every job.",
  "feature_para": "Newer Macomb Township homes often have builder-grade paint that wasn't meant to last much past the first several years, while older properties in the township carry more paint history and prep needs. We scope each differently — newer homes sometimes need less structural prep but more careful color matching against existing trim, while older ones need more scraping and priming before a topcoat will hold.",
  "svc_interior": "Interior painting for Macomb Township homes, whether it's a newer build or a more established property.",
  "svc_exterior": "Exterior painting for Macomb Township properties, with prep scoped to the home's age and condition.",
  "svc_residential": "Residential repaints across Macomb Township, from newer subdivisions to older established streets.",
  "svc_commercial": "Commercial painting for Macomb Township offices, retail spaces, and professional buildings.",
  "local_heading": "Builder-Grade Paint Doesn't Last Forever",
  "local_body": "Newer homes — common throughout Macomb Township's growing subdivisions — are often finished with builder-grade paint chosen for cost, not longevity. It's not unusual for that original coat to show flat spots, uneven sheen, or thin coverage within the first several years, well before a homeowner might expect to repaint. If your home is newer but the paint already looks tired, that's usually the builder-grade finish wearing out on schedule, not a sign anything went wrong — and it's a good opportunity to upgrade to a higher-quality coating that will hold up longer.",
  "faqs": [
    ("Do you offer free estimates in Macomb Township?", "Yes. We provide a free walkthrough and written estimate for homes and businesses throughout Macomb Township."),
    ("My home is newer — why does the paint already look worn?", "Builder-grade paint is typically chosen for cost rather than durability, so it's common to see it wear within the first several years, especially on newer Macomb Township construction."),
    ("Do you work with businesses in Macomb Township?", "Yes. We handle commercial painting for offices, retail, and professional buildings throughout Macomb Township."),
  ],
},

"metamora-mi": {
  "hero": "Metamora is a smaller, more rural community than most of the areas we serve, and homes here often sit on larger lots with more exterior square footage to cover. We handle interior, exterior, residential, and commercial painting with the same owner-led standard, no matter the property size.",
  "feature_para": "Larger lots and standalone properties, more common around Metamora than in denser suburbs, usually mean more exterior surface area and sometimes outbuildings or additional structures to consider. We scope those properties with that in mind during the estimate, rather than pricing by a flat per-project assumption that doesn't account for the extra square footage.",
  "svc_interior": "Interior painting for Metamora homes, from single rooms to full interiors.",
  "svc_exterior": "Exterior painting scoped for larger properties, with prep and coverage planned around the full extent of the home.",
  "svc_residential": "Residential painting for Metamora properties on larger lots, priced to reflect the actual scope of the work.",
  "svc_commercial": "Commercial painting for Metamora-area businesses and professional buildings.",
  "local_heading": "Painting Larger Properties",
  "local_body": "A home on a larger lot — more typical around Metamora than in tighter subdivisions — often has more exterior wall area, and sometimes a detached garage, shed, or other structure that a homeowner wants matched or coordinated with the main house. We walk the full property during the estimate, not just the house itself, so pricing reflects the real scope rather than a flat assumption based on square footage of the home alone.",
  "faqs": [
    ("Do you offer free estimates in Metamora?", "Yes. We provide a free, full-property walkthrough and written estimate for Metamora homes."),
    ("Can you paint outbuildings along with the main house?", "Yes. We can include garages, sheds, or other structures in the same project and coordinate the color scheme with your home."),
    ("Do you paint both interior and exterior properties in Metamora?", "Yes. We handle interior, exterior, residential, and commercial painting throughout Metamora and nearby Oxford, Lake Orion, and Romeo."),
  ],
},

"new-baltimore-mi": {
  "hero": "New Baltimore sits along Anchor Bay, and homes here range from established residential streets to newer waterfront-area development. We handle interior, exterior, residential, and commercial painting with prep suited to whichever your property needs.",
  "feature_para": "Proximity to Anchor Bay means some New Baltimore homes deal with more humidity and moisture exposure than properties further inland, which affects how long paint holds up and how much dry time exterior coats need between applications. We ask about a property's location relative to the water during the estimate, since it changes our approach to prep and product selection.",
  "svc_interior": "Interior painting for New Baltimore homes, from established residential streets to newer construction.",
  "svc_exterior": "Exterior painting with moisture-conscious prep for New Baltimore properties near Anchor Bay.",
  "svc_residential": "Residential repaints for New Baltimore homeowners, scheduled around your household.",
  "svc_commercial": "Commercial painting for New Baltimore's storefronts and professional buildings.",
  "local_heading": "Painting Near the Water",
  "local_body": "Homes closer to Anchor Bay tend to see more humidity in the air than properties further inland, and that affects paint in a couple of ways — it can slow drying time between coats, and it puts more ongoing stress on exterior coatings over the years. For New Baltimore properties near the water, we build in extra dry time during the project and lean toward coatings with better moisture resistance, rather than treating every exterior the same regardless of how close it sits to the bay.",
  "faqs": [
    ("Do you offer free estimates in New Baltimore?", "Yes. We provide a free walkthrough and written estimate for New Baltimore homes and businesses."),
    ("Do you use different coatings for homes near Anchor Bay?", "Where it's warranted, yes — homes closer to the water benefit from more moisture-resistant coatings, which we can discuss during your estimate."),
    ("Do you work with businesses in New Baltimore?", "Yes. We handle commercial painting for storefronts and professional buildings throughout New Baltimore."),
  ],
},

"oakland-township": {
  "hero": "Oakland Township is where we're based, and it's the community we know best — interior, exterior, residential, and commercial painting for township homes on every kind of lot, from smaller subdivisions to larger standalone properties.",
  "feature_para": "As a township rather than a dense city, Oakland Township has a wider range of lot sizes and home styles than a typical suburb, and often more exterior square footage per property. We scope each job on its own during the walkthrough, and because this is our home base, scheduling flexibility here tends to be a little easier than it is further out.",
  "svc_interior": "Interior painting for Oakland Township homes, from single-room updates to full-house repaints.",
  "svc_exterior": "Exterior painting scoped for the township's larger lots, with coverage planned around each property's full footprint.",
  "svc_residential": "Residential painting for Oakland Township properties of every size, handled by our home-base crew.",
  "svc_commercial": "Commercial painting for offices and professional spaces in and around Oakland Township.",
  "local_heading": "Painting Homes in Oakland Township",
  "local_body": "Oakland Township is our home base, which means most projects here don't involve much drive time, and scheduling tends to have a bit more flexibility as a result. The township's mix of subdivisions and larger standalone lots means property size varies more than in a typical dense suburb, so we walk the full lot during the estimate — house, and any additional structures — rather than pricing from a flat assumption. Being local also means if something needs a follow-up visit after the job is done, that's a short trip, not a scheduling hassle.",
  "faqs": [
    ("Do you offer free estimates in Oakland Township?", "Yes. Since this is our home base, scheduling an estimate in Oakland Township is often easier to fit in quickly."),
    ("Do you paint both interior and exterior properties in Oakland Township?", "Yes. We handle interior, exterior, residential, and commercial painting throughout Oakland Township and nearby Rochester Hills, Rochester, and Lake Orion."),
    ("Are you licensed and insured in Oakland Township?", "Yes. Tim MacDonough Painting Company is fully licensed and insured, based right here in Oakland Township."),
  ],
},

"orchard-lake-mi": {
  "hero": "Orchard Lake homes range from lakefront properties to inland residential streets, and we scope each differently — interior, exterior, residential, and commercial painting with prep suited to whichever kind of property you have.",
  "feature_para": "As the name suggests, Orchard Lake has real lakefront exposure for some properties, which means more humidity and reflected sun on those homes than on inland ones a few blocks away. We ask where a property sits relative to the water during the estimate, since lakefront exteriors typically need more moisture-conscious prep and coatings than an inland home in the same area.",
  "svc_interior": "Interior painting for Orchard Lake homes, from lakefront properties to inland residential streets.",
  "svc_exterior": "Exterior painting with moisture-conscious prep for Orchard Lake's waterfront and near-water properties.",
  "svc_residential": "Residential repaints for Orchard Lake homeowners, whether your property is on the water or set back from it.",
  "svc_commercial": "Commercial painting for offices and professional spaces in and around Orchard Lake.",
  "local_heading": "Lakefront vs. Inland: Different Exposure, Different Prep",
  "local_body": "Not every Orchard Lake property faces the same conditions. A home directly on the water deals with more humidity, more reflected sunlight, and often more wind exposure than a similar home set back in an inland subdivision. That difference matters for exterior painting — lakefront homes generally benefit from moisture-resistant coatings and a bit more dry time between coats, while inland properties can often follow a more standard exterior process. We factor in where your home actually sits, rather than treating every Orchard Lake exterior the same.",
  "faqs": [
    ("Do you offer free estimates in Orchard Lake?", "Yes. We provide a free walkthrough and written estimate for Orchard Lake homes, lakefront or inland."),
    ("Do you paint lakefront homes in Orchard Lake?", "Yes. We use moisture-resistant coatings and extra prep time on lakefront and near-water properties."),
    ("Do you paint both interior and exterior properties in Orchard Lake?", "Yes. We handle interior, exterior, residential, and commercial painting throughout Orchard Lake and nearby West Bloomfield, Sylvan Lake, and Bloomfield Hills."),
  ],
},

"oxford-mi": {
  "hero": "Oxford has a mix of established village homes and newer subdivisions further out, and we handle interior, exterior, residential, and commercial painting for both, scoped individually rather than priced from a single template.",
  "feature_para": "Homes closer to Oxford's village center tend to be older, with more original trim and plaster to work around, while properties in newer subdivisions further out are usually straightforward builder-grade construction that's due for an upgrade coat. We scope each differently during the walkthrough, since the prep requirements aren't the same.",
  "svc_interior": "Interior painting for Oxford homes, from village-area properties to newer subdivision construction.",
  "svc_exterior": "Exterior painting for Oxford properties, with prep matched to each home's age and construction.",
  "svc_residential": "Residential repaints for Oxford homeowners across the village and surrounding subdivisions.",
  "svc_commercial": "Commercial painting for Oxford's storefronts, offices, and professional spaces.",
  "local_heading": "Interior Painting Ideas for Oxford Homes",
  "local_body": "A full repaint isn't always necessary to refresh a home — sometimes updating trim to a crisp white against a deeper wall color, or repainting just the entryway and main living areas, makes the biggest visible difference for the smallest project. For Oxford homes with a mix of older and newer construction throughout the area, we're happy to talk through options during the estimate, whether that's a single accent room, a full interior repaint, or just updating trim and doors without touching the walls.",
  "faqs": [
    ("Do you offer free estimates in Oxford?", "Yes. We provide a free walkthrough and written estimate for Oxford homes and businesses."),
    ("Can you help with color selection?", "Yes. We can talk through color and sheen options during your estimate, whether you're updating one room or the whole house."),
    ("Do you paint both interior and exterior properties in Oxford?", "Yes. We handle interior, exterior, residential, and commercial painting throughout Oxford and nearby Lake Orion, Metamora, and Romeo."),
  ],
},

"pleasant-ridge-mi": {
  "hero": "Pleasant Ridge is one of the smallest cities we serve, and homes here are close together on tree-lined streets — which means careful staging and protection matter as much as the paint itself. We handle interior, exterior, residential, and commercial painting with that in mind.",
  "feature_para": "With homes set close together, exterior work in Pleasant Ridge requires more attention to containment — where ladders and equipment sit, how overspray is controlled, and making sure a neighbor's property isn't affected by work happening on yours. We plan that staging as part of the estimate, not as an afterthought once the crew shows up.",
  "svc_interior": "Interior painting for Pleasant Ridge homes, finished cleanly with careful attention to trim and ceilings.",
  "svc_exterior": "Exterior painting for Pleasant Ridge's close-set homes, with equipment and overspray carefully contained.",
  "svc_residential": "Residential repaints for Pleasant Ridge homeowners, from single rooms to full-property projects.",
  "svc_commercial": "Commercial painting for small businesses and offices in and around Pleasant Ridge.",
  "local_heading": "Painting on a Tighter Lot",
  "local_body": "Close-together homes are common in Pleasant Ridge, and that changes how a paint job gets run. Ladders, tarps, and paint stations need a plan before the first coat goes on, and exterior work has to account for a neighbor's fence or driveway a few feet away. We walk the property line with you before we start, agree on where equipment will sit, and keep the work area contained so the project doesn't spill onto property that isn't ours to paint.",
  "faqs": [
    ("Do you offer free estimates in Pleasant Ridge?", "Yes. We provide a free walkthrough and written estimate for Pleasant Ridge homes."),
    ("How do you handle overspray and equipment staging on smaller lots?", "We mask and tape thoroughly and keep equipment contained to your property line, which we pay close attention to in tighter neighborhoods like Pleasant Ridge."),
    ("Do you paint both interior and exterior properties in Pleasant Ridge?", "Yes. We handle interior, exterior, residential, and commercial painting throughout Pleasant Ridge and nearby Royal Oak, Huntington Woods, and Berkley."),
  ],
},

"rochester-mi": {
  "hero": "Rochester's historic downtown sits alongside newer residential growth throughout the city, and we handle interior, exterior, residential, and commercial painting for both — older buildings that need careful prep and newer homes that need a clean, precise finish.",
  "feature_para": "Properties near Rochester's historic downtown often carry more paint history and original architectural detail than newer construction elsewhere in the city, which means more prep time — scraping, sanding, priming — before a topcoat will hold properly. We scope downtown-adjacent and newer properties differently rather than pricing every Rochester job the same way.",
  "svc_interior": "Interior painting for Rochester homes, from downtown-adjacent properties to newer residential construction.",
  "svc_exterior": "Exterior painting for Rochester properties, with prep scoped to each building's age and history.",
  "svc_residential": "Residential repaints for Rochester homeowners throughout the city's older and newer neighborhoods.",
  "svc_commercial": "Commercial painting for Rochester's downtown storefronts and professional office spaces.",
  "local_heading": "Choosing a Painter Near Downtown Rochester",
  "local_body": "Older buildings near Rochester's downtown often come with more architectural detail worth preserving — original trim profiles, storefront cornices, brick that needs careful masking rather than overspray. When you're hiring a painter for a property like this, ask specifically how they handle masonry and trim detail, and whether they've worked on older commercial or residential buildings before. We treat that kind of detail work as its own category, not an afterthought tacked onto a standard repaint.",
  "faqs": [
    ("Do you offer free estimates in Rochester?", "Yes. We provide a free walkthrough and written estimate for homes and businesses throughout Rochester."),
    ("Can you paint older or historic buildings near downtown Rochester?", "Yes. We're comfortable working with original trim, masonry, and architectural detail common in older Rochester properties."),
    ("Do you work with businesses near downtown Rochester?", "Yes. We handle commercial painting for storefronts and offices throughout Rochester's downtown and surrounding areas."),
  ],
},

"romeo-mi": {
  "hero": "Romeo's neighborhood streets and established homes call for a painter who treats every job like it's on their own street — interior, exterior, residential, and commercial painting from a crew that shows up prepared and finishes clean.",
  "feature_para": "A lot of Romeo's housing stock is established rather than new, which usually means more original trim and prior paint layers to work through during prep. We don't rush that step. Scraping loose paint, sanding rough edges, and priming bare wood before color goes on is what determines whether a repaint lasts five years or fifteen.",
  "svc_interior": "Interior painting for Romeo's established homes, with real prep time for original trim and older walls.",
  "svc_exterior": "Exterior painting built to last through Michigan winters, with thorough scraping and priming before any topcoat.",
  "svc_residential": "Residential repaints for Romeo homeowners, from single-room updates to full-property projects.",
  "svc_commercial": "Commercial painting for Romeo's small businesses and professional offices.",
  "local_heading": "When Is It Time to Repaint?",
  "local_body": "Interior walls usually show their age gradually — scuffed corners, a duller sheen, or a color that no longer fits the room. Exteriors give more obvious warning signs: paint that chalks off on your hand when you touch it, visible cracking, or bare wood showing at trim joints. For a community like Romeo with a lot of established housing stock, catching those signs early usually means a straightforward repaint — waiting until moisture gets underneath the failing paint turns it into a repair instead.",
  "faqs": [
    ("Do you offer free estimates in Romeo?", "Yes. We provide a free walkthrough and written estimate for Romeo homes and businesses."),
    ("How do I know if my exterior needs painting or repair?", "Chalking, minor cracking, and fading usually mean it's time to repaint. Soft or rotting wood, or paint that's peeled down to bare material in multiple spots, may need repair work first — we'll flag that during the estimate."),
    ("Do you paint both interior and exterior properties in Romeo?", "Yes. We handle interior, exterior, residential, and commercial painting throughout Romeo and nearby Washington Township, Oxford, and Metamora."),
  ],
},

"royal-oak-mi": {
  "hero": "Royal Oak is one of the busier communities we serve, with homes ranging from classic bungalows to updated interiors near downtown. We handle interior, exterior, residential, and commercial painting throughout the city, scoped to fit each property.",
  "feature_para": "Royal Oak's density means homes are often closer together than in surrounding suburbs, and a mix of older bungalows and updated renovations means prep needs vary block to block. We scope each Royal Oak project individually — checking trim condition, prior paint layers, and lot spacing — rather than pricing from a flat citywide assumption.",
  "svc_interior": "Interior painting for Royal Oak's bungalows and updated interiors, with trim and ceiling work finished cleanly.",
  "svc_exterior": "Exterior painting for Royal Oak homes, with careful staging suited to closer-set city lots.",
  "svc_residential": "Residential repaints for Royal Oak homeowners, from classic bungalows to renovated properties.",
  "svc_commercial": "Commercial painting for Royal Oak's offices, retail spaces, and restaurants.",
  "local_heading": "Painting on a Tighter City Lot",
  "local_body": "Closer-set homes are common throughout Royal Oak, and that changes how exterior work gets staged — where ladders and equipment sit, how overspray is controlled, and keeping a neighbor's driveway or fence line clear. We walk the property line with you before starting, agree on where equipment will go, and keep the work area contained so a Royal Oak project doesn't spill onto property that isn't ours to paint.",
  "faqs": [
    ("Do you offer free estimates in Royal Oak?", "Yes. We provide a free walkthrough and written estimate for Royal Oak homes and businesses."),
    ("Do you paint bungalows and older Royal Oak homes?", "Yes. We're comfortable working with original trim and older construction common throughout Royal Oak's bungalow neighborhoods."),
    ("Do you work with businesses in Royal Oak?", "Yes. We handle commercial painting for offices, retail, and restaurant spaces throughout Royal Oak."),
  ],
},

"sterling-heights-mi": {
  "hero": "Sterling Heights is one of the larger communities we serve, with a wide range of home ages and styles across the city. We handle interior, exterior, residential, and commercial painting throughout, scoped individually rather than priced from a single template.",
  "feature_para": "A city the size of Sterling Heights covers a lot of different housing stock — established neighborhoods with older homes, and newer subdivisions with builder-grade construction that's due for an upgrade. We scope each project during the walkthrough based on the actual property, not a citywide assumption about what a typical Sterling Heights home needs.",
  "svc_interior": "Interior painting for Sterling Heights homes, across both established neighborhoods and newer construction.",
  "svc_exterior": "Exterior painting for Sterling Heights properties, with prep scoped to each home's age and condition.",
  "svc_residential": "Residential repaints for Sterling Heights homeowners throughout the city's varied neighborhoods.",
  "svc_commercial": "Commercial painting for Sterling Heights offices, retail spaces, and professional buildings.",
  "local_heading": "What Sterling Heights Property Owners Should Consider Before Repainting",
  "local_body": "Before scheduling a repaint, it's worth deciding what's actually driving the project — is the current paint failing (chalking, cracking, peeling), or is this a cosmetic update to a color that's simply dated? The two call for different scopes: failing paint needs real prep work before a topcoat will hold, while a cosmetic update on sound paint can often move straight to color with lighter prep. We ask about that distinction during the Sterling Heights estimate so the scope — and price — matches what your property actually needs.",
  "faqs": [
    ("Do you offer free estimates in Sterling Heights?", "Yes. We provide a free walkthrough and written estimate for homes and businesses throughout Sterling Heights."),
    ("Do you work with businesses in Sterling Heights?", "Yes. We handle commercial painting for offices, retail, and professional buildings throughout Sterling Heights."),
    ("What surfaces can you paint?", "Interior walls, trim, ceilings, and cabinets, along with exterior siding, trim, doors, shutters, and porches."),
  ],
},

"sylvan-lake-mi": {
  "hero": "Sylvan Lake is one of Michigan's smallest cities, built around the lake it's named for, and homes here — many with real lakefront exposure — need exterior painting that accounts for that. We handle interior, exterior, residential, and commercial painting with moisture-conscious prep where it's needed.",
  "feature_para": "Being a small lake-centered city, a large share of Sylvan Lake properties deal with more humidity and reflected sun than an inland home would. We ask where a property sits relative to the water during the estimate, since lakefront exteriors typically need more moisture-resistant coatings and a bit more dry time between coats than a home set back from the shoreline.",
  "svc_interior": "Interior painting for Sylvan Lake homes, from lakefront cottages to inland properties.",
  "svc_exterior": "Exterior painting with moisture-conscious prep and coatings for Sylvan Lake's waterfront properties.",
  "svc_residential": "Residential repaints for Sylvan Lake homeowners, on the water or set back from it.",
  "svc_commercial": "Commercial painting for professional and office spaces in and around Sylvan Lake.",
  "local_heading": "Painting a Lakefront Property",
  "local_body": "A water-facing exterior wears differently than the rest of a home — more reflected sun, more humidity, and often more direct wind exposure. On a lakefront property in Sylvan Lake, we typically plan for that side to need a more moisture-resistant coating and a closer eye during the estimate for early signs of wear, like chalking or hairline cracking near trim. It's worth budgeting slightly more attention there than you would on an inland home, since that side of the house is doing more work.",
  "faqs": [
    ("Do you paint lakefront homes in Sylvan Lake?", "Yes. We use moisture-resistant coatings and extra prep time on lakefront and near-water properties throughout Sylvan Lake."),
    ("Do you offer free estimates in Sylvan Lake?", "Yes. We provide a free walkthrough and written estimate for Sylvan Lake homes."),
    ("Do you paint both interior and exterior properties in Sylvan Lake?", "Yes. We handle interior, exterior, residential, and commercial painting throughout Sylvan Lake and nearby Orchard Lake, West Bloomfield, and Bloomfield Hills."),
  ],
},

"troy-mi": {
  "hero": "Troy is one of the larger communities we serve, with everything from established neighborhoods to newer commercial corridors. We handle interior, exterior, residential, and commercial painting throughout the city, scoped individually so pricing reflects your actual property.",
  "feature_para": "A city the size of Troy covers a lot of ground — established residential streets with older homes, newer subdivisions, and busy commercial corridors near the business district. We scope each project on its own during the walkthrough rather than pricing from a flat citywide assumption, since an older home's prep needs look nothing like a newer office buildout's.",
  "svc_interior": "Interior painting for Troy homes, from established neighborhoods to newer residential construction.",
  "svc_exterior": "Exterior painting for Troy properties, with prep scoped to each home's age and exposure.",
  "svc_residential": "Residential repaints for Troy homeowners across the city's older and newer neighborhoods.",
  "svc_commercial": "Commercial painting for Troy's offices, retail spaces, and business-corridor properties.",
  "local_heading": "Choosing a Painter in Troy",
  "local_body": "In a city with as many painting contractors as Troy, it's worth asking a few direct questions before hiring one: Is the estimate written and itemized, or a verbal ballpark? Is the crew doing the work employed directly, or subcontracted out for the day? How many coats are included, and is surface prep — scraping, sanding, priming — spelled out or assumed? We're owner-operated with no subcontractors, which means the person who quotes your Troy project is accountable for how it turns out, not just how it's priced.",
  "faqs": [
    ("Do you offer free estimates in Troy?", "Yes. Free estimates are available for Troy homes and businesses. We provide an owner-led walkthrough and a clear written proposal."),
    ("Do you paint both interior and exterior properties in Troy?", "Yes. We handle interior painting, exterior painting, residential painting, and commercial painting throughout Troy and nearby Birmingham, Rochester Hills, and Royal Oak."),
    ("Are you licensed and insured in Troy?", "Yes. Tim MacDonough Painting Company is fully licensed and insured for all painting work in Troy and surrounding areas."),
  ],
},

"utica-mi": {
  "hero": "Utica combines an older downtown core with newer residential growth nearby, and we handle interior, exterior, residential, and commercial painting for both — older buildings that need careful prep and newer homes that need a clean, precise finish.",
  "feature_para": "Properties near Utica's older downtown core typically carry more paint history and original trim detail than newer construction nearby, which changes the prep timeline. We scope downtown-area and newer properties differently, since one usually needs more scraping and priming while the other needs more careful masking for crisp, clean lines.",
  "svc_interior": "Interior painting for Utica homes, from older downtown-area properties to newer residential construction.",
  "svc_exterior": "Exterior painting for Utica properties, with prep matched to each building's age and history.",
  "svc_residential": "Residential repaints for Utica homeowners throughout the city's older and newer neighborhoods.",
  "svc_commercial": "Commercial painting for Utica's downtown storefronts and professional office spaces.",
  "local_heading": "Planning Your Painting Project",
  "local_body": "The most useful thing a homeowner or business owner can do before painters arrive is decide on scope and priorities up front — is this a single room, a full interior, the exterior, or a storefront that needs to stay open during the work? We walk Utica properties in detail during the estimate so nothing gets missed and so the written proposal reflects the property's actual condition, whether it's an older building near downtown or a newer home nearby.",
  "faqs": [
    ("Do you offer free estimates in Utica?", "Yes. We provide a free walkthrough and written estimate for homes and businesses throughout Utica."),
    ("Can you paint a storefront while staying open for business?", "Yes. We can schedule commercial work in phases or after hours to minimize disruption to your Utica business."),
    ("Do you paint both interior and exterior properties in Utica?", "Yes. We handle interior, exterior, residential, and commercial painting throughout Utica and nearby Shelby Township, Sterling Heights, and Clinton Township."),
  ],
},

"washington-township-mi": {
  "hero": "Washington Township has more rural and larger-lot properties than a typical suburb, and homes here often mean more exterior square footage to plan for. We handle interior, exterior, residential, and commercial painting with pricing based on your property's actual scope.",
  "feature_para": "Larger lots and standalone properties, common throughout Washington Township, usually mean more exterior wall area and sometimes additional structures — a garage, barn, or outbuilding — that a homeowner wants included in the project. We walk the full property during the estimate rather than pricing from a flat per-project assumption that doesn't account for the extra ground covered.",
  "svc_interior": "Interior painting for Washington Township homes, from single rooms to full interiors.",
  "svc_exterior": "Exterior painting scoped for larger properties, with coverage planned around the full extent of the home.",
  "svc_residential": "Residential painting for Washington Township properties on larger lots, priced to reflect the real scope of work.",
  "svc_commercial": "Commercial painting for Washington Township businesses and professional buildings.",
  "local_heading": "Painting Larger Properties",
  "local_body": "A home on a larger lot — common throughout Washington Township — often has more exterior wall area, and sometimes a detached garage, barn, or other structure a homeowner wants matched or coordinated with the main house. We walk the full property during the estimate, not just the house itself, so pricing reflects the real scope rather than a flat assumption based on the home's square footage alone.",
  "faqs": [
    ("Do you offer free estimates in Washington Township?", "Yes. We provide a free, full-property walkthrough and written estimate for Washington Township homes."),
    ("Can you paint outbuildings along with the main house?", "Yes. We can include garages, barns, or other structures in the same project and coordinate the color scheme with your home."),
    ("Do you paint both interior and exterior properties in Washington Township?", "Yes. We handle interior, exterior, residential, and commercial painting throughout Washington Township and nearby Romeo, Macomb Township, and Lake Orion."),
  ],
},

"lake-orion": {
  "hero": "Lake Orion's township properties often sit on larger lots with more exterior square footage than a typical subdivision home, and we scope every project accordingly — interior, exterior, residential, and commercial painting priced to match your actual property.",
  "feature_para": "Township living around Lake Orion tends to mean larger lots, longer driveways, and more standalone exterior surface area than a dense suburb. We walk the full property during the estimate — not just a quick look at the house — so pricing reflects the real scope, and we plan exterior work with enough time to properly prep and coat a larger home rather than rushing through it.",
  "svc_interior": "Interior painting for Lake Orion homes, from township properties to lakefront cottages.",
  "svc_exterior": "Exterior painting scoped for larger township lots, with full-property prep and coverage planned in advance.",
  "svc_residential": "Residential painting for Lake Orion homeowners, on the water or set back on a larger township lot.",
  "svc_commercial": "Commercial painting for Lake Orion offices, storefronts, and event spaces.",
  "local_heading": "Painting a Lakefront or Larger Township Property",
  "local_body": "Lake Orion covers both real lakefront homes and larger township lots set back from the water, and the two call for different planning. Lakefront exteriors typically need more moisture-resistant coatings and extra dry time between coats, while larger township properties simply need more coverage planned into the schedule so the crew isn't rushing to finish a bigger exterior in the same time as a standard suburban home. We ask which situation applies to your property during the estimate so the plan — and the price — actually fits.",
  "faqs": [
    ("Do you offer free estimates in Lake Orion?", "Yes. Free estimates are available for Lake Orion homes and businesses, including full-property walkthroughs for larger township lots."),
    ("Do you paint lakefront homes in Lake Orion?", "Yes. We use moisture-resistant coatings and extra prep time on lakefront and near-water properties around Lake Orion."),
    ("Are you licensed and insured in Lake Orion?", "Yes. Tim MacDonough Painting Company is fully licensed and insured for all painting work in Lake Orion and surrounding areas."),
  ],
},

"shelby-township": {
  "hero": "Shelby Township covers a wide mix of property types, from established residential streets to newer construction, and we handle interior, exterior, residential, and commercial painting for all of them — scoped individually rather than priced from a flat template.",
  "feature_para": "A township this size means real variation in what a property needs — older homes with more prior paint layers and trim detail, and newer construction with builder-grade paint that's often due for an upgrade well before a homeowner expects. We scope each Shelby Township project during the walkthrough based on the property in front of us, not a generic township-wide assumption.",
  "svc_interior": "Interior painting for Shelby Township homes, across both established neighborhoods and newer construction.",
  "svc_exterior": "Exterior painting for Shelby Township properties, with prep scoped to each home's age and condition.",
  "svc_residential": "Residential repaints for Shelby Township homeowners throughout the township's varied neighborhoods.",
  "svc_commercial": "Commercial painting for Shelby Township offices, retail spaces, and professional buildings.",
  "local_heading": "What Shelby Township Property Owners Should Consider Before Repainting",
  "local_body": "Before scheduling a repaint, it helps to know what's actually driving the project — is the current paint failing (chalking, cracking, peeling), or is this a cosmetic update to a color that's simply dated? The two call for different scopes: failing paint needs real prep work before a new coat will hold, while a cosmetic refresh on otherwise sound paint can often move to color with lighter prep. We ask about that distinction during the Shelby Township estimate so the scope — and the price — matches what your property actually needs.",
  "faqs": [
    ("Do you offer free estimates in Shelby Township?", "Yes. We provide a free walkthrough and written estimate for homes and businesses throughout Shelby Township."),
    ("Do you work with businesses in Shelby Township?", "Yes. We handle commercial painting for offices, retail, and professional buildings throughout Shelby Township."),
    ("Do you paint both interior and exterior properties in Shelby Township?", "Yes. We handle interior painting, exterior painting, residential painting, and commercial painting throughout Shelby Township and nearby Macomb Township, Rochester Hills, and Utica."),
  ],
},

}
