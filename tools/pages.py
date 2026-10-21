# Page content. Executed by build.py with its helpers in scope.

GAME_LD = {
    "@context": "https://schema.org", "@type": "VideoGame",
    "name": "PERSIAN STRIKE: RETRIBUTION", "url": ORIGIN,
    "image": ORIGIN + "media/" + IMG["hero"][0],
    "description": "An alternate-history 1990s gulf war: a Desert Strike-style helicopter war crossed with base-building, across four seasonal campaigns. In early access for Windows and Linux PC.",
    "genre": ["Action", "Strategy"], "gamePlatform": ["PC (Microsoft Windows)", "PC (Linux)"],
    "playMode": "SinglePlayer",
    "publisher": {"@type": "Organization", "name": "Reformat Games"},
    "author": {"@type": "Organization", "name": "Reformat Games"},
    "offers": {"@type": "Offer", "url": BUY, "price": "5.00", "priceCurrency": "USD",
               "availability": "https://schema.org/InStock"},
}

# ------------------------------------------------------------------ home
home = f"""
<div class="hero-frame">{img("hero", lazy=False)}</div>
<div class="rule"></div>
<section class="hero-title"><div class="wrap">
  <div>
    <div class="studio">Reformat Games presents</div>
    <h1>Persian Strike<span>Retribution</span></h1>
  </div>
  <div>
    <p class="pitch">One defected battleship. One stolen gunship. A helicopter war in the Desert Strike tradition, crossed with a base you found, feed and defend, all flown from one cockpit.</p>
    <div class="cta"><a class="btn primary" href="{BUY}" target="_blank" rel="noopener">Buy on itch.io</a><a class="btn" href="#trailer">Watch the trailer</a></div>
    <div class="meta">Early access · Windows &amp; Linux PC · Free demo: Operation Tondbad</div>
  </div>
</div></section>

{block(head("Trailer 2", "Watch the war.", "Ninety seconds of the current build. Every shot was flown and filmed in the game, with the game's own sound under the score.") + film("trailer2.mp4", "trailer_poster", "Persian Strike: Retribution", "Trailer 2 · Early access", "One defected battleship, stolen gunships, and his entire war machine: four campaigns, day and night, in every kind of weather."), sid="trailer")}

{block(head("Alternate history", "The war that never happened.", "") + '''<div class="prose">
<p class="lede">A 1990s that never was. In the <b>Republic of Parsava</b>, a fictional country on the Gulf, the oil, the radars and the television all answer to <b>Marshal Rashid al-Ghazi</b>, a foreign-born strongman ruling Persian soil.</p>
<p class="lede">When his Guard fired on the protest squares, the crew of one battleship stopped taking orders. They took the Simorgh, her gunship and every mixtape aboard, and went to war with the regime that trained them. The state news calls them pirates. The villages cheer when they fly over.</p>
</div>''', cls="alt")}

{block(head("Four campaigns · one war", "Spring to the third winter.", "Each campaign is one continuous, hand-authored theater. The war carries over: what you take in spring is who fights beside you in winter.") + f'''<div class="campaigns">
<a class="camp" href="c1.html"><div class="pic">{img("camp_c1")}</div><div class="txt"><div class="num">Campaign I · Spring</div><h3>Operation Tondbad</h3><p>The mutiny in the Gulf of Simorgh. Restore a ruined regime installation into your beachhead, then take the Parsava coast off the war book, one operation at a time.</p><span class="go">Read the campaign →</span></div></a>
<a class="camp" href="c2.html"><div class="pic">{img("camp_c2")}</div><div class="txt"><div class="num">Campaign II · Summer</div><h3>Operation Tangeh</h3><p>The Marshal closes the strait. Free the ports one by one, out-build his fortress across the water, and get the enriched material out without turning the coast to glass.</p><span class="go">Read the campaign →</span></div></a>
<a class="camp" href="c3.html"><div class="pic">{img("camp_c3")}</div><div class="txt"><div class="num">Campaign III · Autumn</div><h3>Operation Shahin</h3><p>The proxy war becomes a world war on the Caspian coast. Slip into the regime's five-pad base under stealth, steal its prototype systems, and stop a sixteen-car armored train.</p><span class="go">Read the campaign →</span></div></a>
<a class="camp" href="c4.html"><div class="pic">{img("camp_c4")}</div><div class="txt"><div class="num">Campaign IV · Three winters later</div><h3>Operation Azadi</h3><p>The movement is the government now. Four contingents, one wall, and a war machine that fights on without its master. Twenty-two minutes on the silo clock.</p><span class="go">Read the campaign →</span></div></a>
</div>''')}

{block(head("The doctrine", "Fly the war. Never command it.", "Desert Strike's cockpit welded to a Command &amp; Conquer economy, and the helicopter is the only cursor you get.") +
split("f_blocks", "Built block by block", "You fly the base in", ["There is no build menu. Ferry the work crew, sling the block tarps off the Simorgh's cargo yard, and watch the building physically go up. Once it stands, its production runs itself.", "Every wall on the beachhead was flown in under your rotors."]) +
split("f_cockpit", "One cockpit", "You never order a unit", ["The ground war is autonomous. Barracks replace their own dead, war factories roll their own columns, and both armies march on authored roads. You change the war by what you carry, what you destroy and who you bring home."], flip=True) +
split("f_demolition", "Destructible", "Everything important breaks", ["Every building, bridge, ship and tower comes apart for real, and the rubble stays where it fell. Drop the only causeway across the strait and you live with the map you made."]), cls="alt")}

{block(head("The living war", "It runs whether you show up or not.", "") + cards([
    ("f_weather", "Weather", "Weather fights too", "Fog seas in the northern valleys, rain on the strait, dust walls on a live wind field and ground blizzards in the third winter. None of it is a skybox."),
    ("f_sea", "The coast", "A war on the water", "Tankers keep their lanes while the shore burns. The sea floats the fleet, stops bullets, and obeys the tide."),
    ("f_livingwar", "Day and night", "The war doesn't stop at dusk", "Tracer, rocket trails and burning palms over a river town at night, with searchlights sweeping for you."),
    ("f_steel", "Oil country", "Everything is full of fuel", "Put a Hellfire into the tank farm and the fire runs tank to tank. Torched derricks burn for hours."),
    ("f_tapes", "Towns", "Towns that live", "Lit windows and parked cars at dusk. Every town was a living place before the war reached it, and traffic still runs its real roads."),
    ("bird_winch", "The gun run", "Rockets, gun, Hellfires", "Hydras for the soft targets, the chin gun for the infantry, Hellfires for the armor and the SAMs."),
], "g3"))}

{block(head("New in the war", "What's flying this update.", "Every picture here is a frame from the current build.") + cards([
    ("new_flares", "Countermeasures", "Flares that burn", "Countermeasures now burn like the real thing: white-hot flares that light up the deck below, each one dragging its own smoke trail down toward the sea."),
    ("new_stealth", "Operation Shahin", "Steal their tech", "In Operation Shahin the squadron steals the regime's own prototypes, including a stealth system that fades the gunship to a ripple in the air."),
    ("new_rain", "Weather", "Rain on the strait", "Rain now falls at raindrop scale, streaking past the bridge cables and across the open water of the strait."),
    ("new_laser", "Operation Tangeh", "The datacenter laser", "Bring the datacenter online and the gunship's laser picks incoming hunter drones out of the dusk on its own."),
    ("new_beards", "People", "Faces of the coast", "A new generation of characters with real beards, moustaches and working headgear: the dock hands, drivers and crews of the Parsava coast."),
], "g3"), cls="alt", sid="new")}

{closer("Out now in early access.", "Four campaigns and one continuous war, with every wall in it flown in under your rotors. Start with the free Operation Tondbad demo, and the war grows with every update.")}
"""
page("index.html", "PERSIAN STRIKE: RETRIBUTION — a helicopter war from Reformat Games",
     "An alternate-history 1990s gulf war: a Desert Strike-style helicopter war crossed with base-building, across four seasonal campaigns. Watch Trailer 2. In early access for Windows and Linux PC.",
     "hero", home, [GAME_LD, video_ld("PERSIAN STRIKE: RETRIBUTION — Trailer 2", "Trailer 2, cut from the current early-access build.", "trailer2.mp4", "trailer_poster")])

# ------------------------------------------------------------------ C1
c1 = campaign_head("Campaign I · Spring", "Operation <span style='color:var(--signal)'>Tondbad</span>",
    "The day the squadron stopped taking orders.", "c1_hero",
    [("Season", "Spring"), ("Theater", "The Parsava coast"), ("Home plate", "The Simorgh"), ("War book", "Nine operations")]) + f"""
{block(head("The cold open", "High noon, the Gulf of Simorgh.", "The actual opening cinematic, captured from the game.") + film("c1_tondbad_opening.mp4", "c1_poster", "Operation Tondbad", "Spring · Campaign I", "The admiral walks the plank, the sharks take the vote, and one battleship, one gunship and every mixtape aboard go to war with the regime that trained them."))}

{block(head("Step one", "You don't get a base. You fly one in.", "Dead abeam the Simorgh's anchorage stands a regime installation the war already chewed through. Everything it will become rides the battleship's deck.") +
split("c1_deck", "Ferry the crew", "Six souls, six seats", ["Land on the Simorgh's pad and the builders run to the skids. Land on the claim and they jump out onto the sand, ready to work."]) +
split("f_blocks", "Sling the tarps", "She flies heavy", ["Hover the cargo yard, winch a tarp of loose blocks and haul it east. Deck riggers lay the bridle before every lift."], flip=True) +
split("c1_beachhead", "The crew builds it", "Roof by roof", ["They restore the ruins in doctrine order: the pit, then rifles, then wheels. When the third roof goes on, the Simorgh opens the war book.", "After that the base runs itself: steel from the pit, riflemen from the barracks, jeeps from the war factory. <b>You fly. The base fights.</b>"]), cls="alt")}

{block(head("The war book", "Nine operations. One coast.", "Every pin on the chart is somewhere you have to fly, in the order you decide.") + cards([
    ("op_c1_01", "Radar", "Blind the Marshal", "Two early-warning radars sweep the coast. Kill both and every regime gun loses a third of its aim and reach."),
    ("op_c1_02", "Power", "Lights out", "One oil-fired station feeds every outlying factory and barracks. Drop it and production stops everywhere but headquarters."),
    ("op_c1_03", "Air defense", "Clear skies", "SAM sites form a belt across the approach. Hellfires are for the SAMs, not the trucks."),
    ("op_c1_04", "Airfield", "Grounded", "The Marshal's Hind squadron sits fueled on the strip. Hit the field and they will scramble."),
    ("op_c1_05", "Rescue", "The pen", "Azadi sailors held in tents beside the Hind strip. Towers first, then open each tent gently."),
    ("op_c1_06", "Rescue", "Press corps", "Three foreign reporters held on the Legation roof as proof that everything is fine. Give the world a close-up of a winch cable instead."),
    ("op_c1_07", "Assault", "Cut the head", "Forward Command on the southern ridge: production, command and fuel. Break it and the headquarters is out of the war."),
    ("op_c1_08", "Capture", "The informant", "The Marshal's spy runs his networks from the command tower. Take him alive; what he knows is worth more than the bunker."),
    ("op_c1_09", "Intel-locked", "Mayday, mayday", "The recon bird went down on day one. The spy knows the grid square. Bring her pilot home and she flies for you."),
], "g3", orders=True))}

{block(head("The country", "Every district was placed by hand.", "Roads first, then the buildings that face them. The Tondbad coast is an authored country, and each district works the way its real counterpart would.") + cards([
    ("c1_pars", "Industry", "The Pars complex", "Field, manifold, tank farm and power plant, laid out in the order the process reads and chained together by pipe. Clip the line anywhere and the fire marches both ways."),
    ("c1_airfield", "Aviation", "The air reservation", "The Hind strip, the prisoner pen, a boneyard of picked-over hulks and a working civil airport inside one perimeter wire."),
    ("c1_oldroad", "Heritage", "The old road", "A bastioned caravanserai and a fire temple burning on its tell. Older than the regime, and it will outlast him."),
    ("c1_qanat", "Water", "Water runs underground", "A qanat shows nothing on the surface. Seven shafts step down from the foothills, and only where the water surfaces does the ground go green."),
    ("c1_town", "Towns", "Towns that live", "Houses with real floor plans, traffic on the actual road graph, and townspeople who scatter when the shooting starts."),
    ("c1_command", "Command", "Forward Command", "The Marshal's citadel on the southern ridge, with its own road, its own armor and its own power. Cut everything else first."),
], "g3"), cls="alt")}

{block(head("Oil country", "Everything here is full of fuel.", "Every tank is full. Rupture one and it doesn't just explode; it pours.") +
split("c1_oilfire", "The spill", "The fire chases the oil", ["Crude finds the real ground under it, and two spills that touch become one pool. The fire front runs out across the film, always a step behind the oil.", "Flame only stands where fuel lies, and leaves the spill only for something worth catching: a tree, a truck, a building."]) +
split("c1_blaze", "The derricks", "A derrick never goes out", ["Torch a rig and it burns standing, a charred lattice wrapped in its own flame, still burning when you fly back at dusk."], flip=True))}

{block(head("From the flight recorder", "Spring, on film.") + gallery([
    ("c1_scale", "The burning coast from altitude", "full"),
    ("c1_hydra", "Rockets into the air-defense site", "wide"), ("c1_derrick", "The oil plant burns", "wide"),
    ("c1_front", "The line of contact", ""), ("c1_warmachine", "His war machine", ""), ("bird_winch", "The gun run", ""),
]), cls="alt")}
{pager(None, ("c2.html", "Operation Tangeh"))}
"""
page("c1.html", "OPERATION TONDBAD — PERSIAN STRIKE: RETRIBUTION",
     "Campaign I, spring on the Parsava coast: the mutiny in the Gulf of Simorgh, a beachhead flown in block by block, nine operations, and an oil country that burns like the real thing.",
     "c1_hero", c1, [video_ld("OPERATION TONDBAD — opening cinematic", "Campaign I opening, captured in-engine.", "c1_tondbad_opening.mp4", "c1_poster")])

# ------------------------------------------------------------------ C2
c2 = campaign_head("Campaign II · Summer", "Operation <span style='color:var(--signal)'>Tangeh</span>",
    "The strait is closed. Open it.", "c2_hero",
    [("Season", "Summer"), ("Theater", "Tangeh-ye Hormoz"), ("Home plate", "Bandar-e Azadi"), ("War book", "Six orders")]) + f"""
{block(head("The cold open", "Day 19, 0300. The strait.", "The actual opening cinematic, captured from the game.") + film("c2_tangeh_opening.mp4", "c2_poster", "Operation Tangeh", "Summer · Campaign II", "The Marshal and his foreign backers close the strait. Bandar-e Azadi holds out on rations and salvage."))}

{block(head("The network", "Every port you free starts producing.", "Bandar-e Azadi opens the campaign as a working stronghold, walls manned, forges lit, and losing. The Marshal's Paygah runs at twice your output.") +
split("c2_bandar", "Home plate", "Bandar-e Azadi", ["The war quarter runs itself: barracks, motor pool and wall batteries, while you fly. Your crew answers the wire; you answer the war."]) +
split("c2_rampart", "The production war", "One war, two colors", ["Both shores build from the same doctrine, gun for gun. The only way to out-build Paygah is to liberate the coast: every freed port raises its own gun and forge and joins the network."], flip=True), cls="alt")}

{block(head("The war book", "Six orders. One strait.", "Each order is a place, and the strait doesn't open until the last of them is done.") + cards([
    ("op_c2_01", "Liberate", "Deh-e Mahi", "The fishing port. Break the garrison and the town raises its own gun and forge."),
    ("op_c2_02", "Liberate", "Bandargah", "The harbor city: cranes, container rows and a garrison dug in among the blocks."),
    ("op_c2_03", "Liberate", "Sahelabad", "The farm-belt town feeding both armies. Whoever holds it eats."),
    ("op_c2_04", "Liberate", "The Zendan", "The prison across the bay. The men inside have waited since the mutiny, and they know how to work a forge."),
    ("op_c2_05", "Recover", "The nuclear material", "The regime enriched it. You deliver it, gently, to ONAT, without turning the coast to glass."),
    ("op_c2_06", "Destroy", "Paygah", "The Marshal's fortress on the far shore. The strait opens over its rubble."),
], "g3", orders=True))}

{block(head("The water runs the war", "The tide has a schedule. So does the storm.", "The Khoshki Bar dries at the ebb and armies walk it. RA'D-O-BARQ rolls in off the gulf and surges it back under.") + cards([
    ("c2_bridge", "The causeway", "Pol-e Azadi", "The one causeway. Every army that wants the far shore queues for it, and it can be destroyed once, forever."),
    ("new_rain", "Weather", "Rain at raindrop scale", "Rain streaks past the bridge cables and rings the open water of the strait."),
    ("c2_refinery", "Oil, again", "The refinery", "The west shore runs on the refinery. Everything in it is full, and everything in it burns."),
    ("c2_citadel", "The storm", "RA'D-O-BARQ", "A slate shelf front, hanging rain shafts and lightning, and a storm surge that rewrites the shoreline while it lasts."),
], "g2"), cls="alt")}

{block(head("From the flight recorder", "Summer, on film.") + gallery([
    ("c2_hero", "The refinery burning at dusk", "wide"), ("f_demolition", "A regime building comes down", "wide"),
    ("new_laser", "The datacenter laser at work", ""), ("new_rain", "Rain on the causeway", ""), ("c2_bridge", "Pol-e Azadi", ""),
]))}
{pager(("c1.html", "Operation Tondbad"), ("c3.html", "Operation Shahin"))}
"""
page("c2.html", "OPERATION TANGEH — PERSIAN STRIKE: RETRIBUTION",
     "Campaign II, summer on the strait: liberate the ports, out-build the Marshal's fortress, ride the tide and the storm, and get the enriched material out.",
     "c2_hero", c2, [video_ld("OPERATION TANGEH — opening cinematic", "Campaign II opening, captured in-engine.", "c2_tangeh_opening.mp4", "c2_poster")])

# ------------------------------------------------------------------ C3
c3 = campaign_head("Campaign III · Autumn", "Operation <span style='color:var(--signal)'>Shahin</span>",
    "The proxy war becomes a world war on the Caspian coast.", "c3_hero",
    [("Season", "Autumn"), ("Theater", "The Caspian coast"), ("The prize", "Five stolen systems"), ("The threat", "A 16-car train")]) + f"""
{block(head("The cold open", "Autumn. The Caspian front.", "One uninterrupted camera: the armored train at its station in the fog, the seawall town, the beach, the rice cooperative, the regime's five-pad base, and finally your gunship, cloaked, coming over the mountains.") + film("c3_shahin_opening.mp4", "c3_poster", "Operation Shahin", "Autumn · Campaign III", "Fog in the valleys, rain on the coast, and the words nobody wanted to say out loud: world war."))}

{block(head("Steal the battle core", "Go in quiet. Come out heavy.", "The regime's eastern base is five armored pads, each guarded by hunting searchlights. Each pad hides a prototype system worth stealing.") +
split("new_stealth", "Stealth", "The approach", ["Your gunship arrives cloaked and only flickers back into view as it lands. A clean winch trip raises no alarm, and a quiet pad sends nothing after you."]) +
split("c3_airhead", "Searchlights", "Every beam is a tripwire", ["Each searchlight answers to its nearest pad. Get caught in the beam, or shoot the lamp, and that pad's alarm sounds: a ten-vehicle detachment drives out of the regime tunnel and its factory starts mobilizing.", "Attack the base before you take the battle core and all five pads wake at once. <b>That is the deliberate bad idea.</b>"], flip=True), cls="alt")}

{block(head("The war book", "Five steals, one train, one alliance.", "Shahin's orders open as you earn them. Every stolen system is physical cargo, flown across the map on your winch line and seated on its matching pad in the west.") + cards([
    ("c3_port", "Steal", "The battle core", "Lift the glowing gyroscopic core off the eastern pad and lower it onto its receiver in the west. Only then is it yours."),
    ("c3_train", "Destroy", "The battle train", "Sixteen armored cars out of the Shahin station: SAM cars, anti-aircraft mounts and twin cannon turrets behind a locomotive that throws its own flares."),
    ("c3_autumn", "Steal", "The five-pad line", "Fire control, anti-air, experimental power and the datacenter. Each lift takes the bonus from the enemy and brings a western pad online for you."),
    ("c3_darkpad", "Hold", "The northern landings", "ONAT and RKA landing ships come ashore from opposite ends of the Caspian and collide in the town at the center. Hold your whole line while they do."),
], "g2", orders=True))}

{block(head("The north", "A different country.", "") + '''<p class="lede">Slate-teal Caspian water and an olive sediment shelf. A seawall town, an open public beach, marsh walks, a working rice plain and rail industries, all of them living places before the war reaches them. Copper Hyrcanian forest climbs toward the Alborz snowline, and the weather moves from rain to mist to sleet to snow.</p>''', cls="alt")}

{block(head("From the flight recorder", "Autumn, on film.") + gallery([
    ("c3_train", "The battle train in the fog", "wide"), ("new_stealth", "Cloaked over the paddies", "wide"),
    ("c3_port", "The Caspian harbor", ""), ("c3_airhead", "The airhead at dawn", ""), ("c3_darkpad", "Overhead, in the first snow", ""),
]))}
{pager(("c2.html", "Operation Tangeh"), ("c4.html", "Operation Azadi"))}
"""
page("c3.html", "OPERATION SHAHIN — PERSIAN STRIKE: RETRIBUTION",
     "Campaign III, autumn on the Caspian coast: slip into the regime's five-pad base under stealth, steal its prototype systems, stop a sixteen-car armored train, and hold the line as two alliances land.",
     "c3_hero", c3, [video_ld("OPERATION SHAHIN — opening cinematic", "Campaign III opening, captured in-engine.", "c3_shahin_opening.mp4", "c3_poster")])

# ------------------------------------------------------------------ C4
c4 = campaign_head("Campaign IV · Three winters later", "Operation <span style='color:var(--signal)'>Azadi</span>",
    "The last mission order is the squadron's own name.", "c4_hero",
    [("Season", "Winter"), ("Theater", "The Daryush Basin"), ("The aircraft", "Khoshgeleh"), ("The clock", "22:00")]) + f"""
{block(head("The cold open", "Everyone answered.", "The actual opening cinematic, captured from the game.") + film("c4_azadi_opening.mp4", "c4_poster", "Operation Azadi", "Winter · Campaign IV", "Three winters on, the Azadi movement is the government of Parsava, and al-Ghazi has wrapped the old capital in a war machine that fights on without him."))}

{block(head("Three winters later", "The war changed who could fight it.", "") + '''<div class="prose">
<p class="lede">The liberated government, chaired by resistance organizer <b>Laleh Farzan</b>, is now recognized. The Tondbad veterans hold the line, the Tangeh corps brings armor and logistics, the Shahin wing brings counter-machine aircraft, and an international column supports rather than replaces them.</p>
<p class="lede">The cask from Tangeh exposed the nuclear program and denied the Marshal most of his stock. One assembled warhead escaped. It sits in a silo under the Daryush Basin.</p>
</div>''', cls="alt")}

{block(head("The aircraft and the clock", "Generous, because it has to be.", "") +
split("c4_khoshgeleh", "The Khoshgeleh", "The black box pays off", ["The prototype recovered in Shahin returns as the Khoshgeleh: double fuel, double gun ammunition, double rockets, the same Hellfire rack, and a belly laser that recharges more than twice as fast as the Shahbaz's.", "The generosity is a warning."]) +
split("c4_silo", "The silo", "Twenty-two minutes", ["After the briefing a nuclear launch timer starts. It drives the physical silo stages, it stops only when the launch is destroyed, and it can fail exactly once, in plain view."], flip=True))}

{block(head("The theater", "The capital, consumed.", "The megabase has eaten the western districts of the national capital. Ruined boulevards, the parliament, the airport, stadium, rail yards and hospital are still readable beneath the machine works.") + cards([
    ("c4_hero", "The enemy", "The megabase", "Five war factories and six repair-lattice cores feed a machine that rebuilds what you break. Kill the cores and it stops healing."),
    ("c4_firstlight", "The east", "The wall", "The whole east is the Azadi zone: the main stronghold, a north camp, and a concrete wall the height of the map, opened at three push roads and covered by four turrets."),
    ("c4_winter", "The aftermath", "First light", "Establish the forward bases, break the swarm, kill the cores, stop the launch. At first light, Parsava is free."),
], "g3"), cls="alt")}
{pager(("c3.html", "Operation Shahin"), ("about.html", "About the studio"))}
"""
page("c4.html", "OPERATION AZADI — PERSIAN STRIKE: RETRIBUTION",
     "Campaign IV, three winters later: fly the Khoshgeleh into a self-healing megabase over the snowbound capital and stop the last nuclear launch with twenty-two minutes on the clock.",
     "c4_hero", c4, [video_ld("OPERATION AZADI — opening cinematic", "Campaign IV opening, captured in-engine.", "c4_azadi_opening.mp4", "c4_poster")])

# ------------------------------------------------------------------ about
about = f"""
<section class="page-head"><div class="wrap">
  <div class="num">The studio · the fine print</div><h1>About</h1>
  <p class="lede">Old formats, reformatted.</p>
</div></section>
<div class="rule"></div>
{block(head("The studio", "Reformat Games.", "") + f'''<div class="prose">
<p class="lede">Reformat Games is an independent studio with a soft spot for the machines and genres the industry left behind: cartridge-era strike games, cassette mixtapes, and action movies that play it ninety percent straight.</p>
<p class="lede"><b>PERSIAN STRIKE: RETRIBUTION</b> is our love letter to all three: a Desert Strike-style helicopter war, rebuilt with a living battlefield and a base you raise block by block. It is in early access for Windows and Linux PC, and the war grows with every update.</p>
</div>
<div class="cta" style="margin-top:28px"><a class="btn primary" href="{BUY}" target="_blank" rel="noopener">Buy on itch.io</a></div>''')}
{block(head("Legal", "The fine print.", "") + '''<div class="legal">
<h3>A work of fiction</h3>
<p>PERSIAN STRIKE: RETRIBUTION is set in an alternate-history 1990s in the fictional Republic of Parsava. All names, characters, places, factions, flags and events are fictional. The game depicts no real state, government, armed force, organization or person, and any resemblance to real ones, living or dead, is coincidental.</p>
<h3>Copyright</h3>
<p>© 2026 Reformat Games LLC. PERSIAN STRIKE: RETRIBUTION, its title treatment, artwork, characters and original content are the property of Reformat Games. The images and films on this site are captured in-engine from the early-access build and may differ from the current version.</p>
<h3>Third-party content</h3>
<p>The game is built with the free and open-source Godot Engine (MIT license). Art assets are original or sourced from public-domain (CC0) libraries and openly licensed (CC-BY) work, with full attribution shipped in the game's credits. Thank you to everyone who keeps the commons alive.</p>
<h3>This website</h3>
<p>This is a static site hosted on GitHub Pages. It sets no cookies and runs no analytics or trackers. GitHub may keep standard server logs under the GitHub privacy statement, and fonts load from Google Fonts under Google's privacy policy.</p>
</div>''', cls="alt")}
"""
page("about.html", "About — PERSIAN STRIKE: RETRIBUTION",
     "Reformat Games, the studio behind PERSIAN STRIKE: RETRIBUTION, and the fine print: a work of fiction, copyright, third-party content and site privacy.",
     "hero", about)
