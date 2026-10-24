"""All site copy, lifted from the brief. Edit here, then rebuild."""

SITE = {
    "name": "SARA AZIZA",
    "tagline": "AN ONGOING COLLECTION OF CURIOSITIES",
    "year": 2026,
    "nav": [
        ("THE COVER", "/"),
        ("THE ARCHIVE", "/archive/"),
        ("THE ARTIST", "/artist/"),
        ("STUDIO NOTES", "/notes/"),
        ("ENQUIRIES", "/enquiries/"),
    ],
    "footer_nav": [
        ("THE COVER", "/"),
        ("THE ARCHIVE", "/archive/"),
        ("THE ARTIST", "/artist/"),
        ("STUDIO NOTES", "/notes/"),
        ("UNFINISHED BUSINESS", "/unfinished/"),
        ("ENQUIRIES", "/enquiries/"),
    ],
    # Where the enquiry form sends. Leave empty to fall back to a mailto: link.
    "form_action": "",
    "contact_email": "hello@saraaziza.com",
}

COLLECTIONS = [
    {
        "number": 1, "slug": "faces-and-familiar-strangers",
        "title": "FACES & FAMILIAR STRANGERS",
        "strap": "People I know. People I don't. People everyone knows.",
        "feeling": "An intimate portrait exhibition.",
        "annotation": "Some faces are just more interesting to draw.",
        "layout": "portrait-right",
    },
    {
        "number": 2, "slug": "under-the-surface",
        "title": "UNDER THE SURFACE",
        "strap": "Anatomy, architecture, engineering, and other things I wanted to take apart (on paper).",
        "feeling": "Leonardo da Vinci's sketchbook meets contemporary design.",
        "fig": "FIG. 002 — A STUDY OF STRUCTURE",
        "annotation": "I have a lot of questions about how things work.",
        "layout": "technical-left",
    },
    {
        "number": 3, "slug": "objects-of-affection",
        "title": "OBJECTS OF AFFECTION",
        "strap": "Things that probably didn't need a portrait of their own.",
        "feeling": "Quiet luxury, still-life photography, beautiful everyday things.",
        "annotation": "I thought it deserved a moment.",
        "layout": "still-life",
    },
    {
        "number": 4, "slug": "places-ive-been",
        "title": "PLACES I'VE BEEN (AND SOME I HAVEN'T)",
        "strap": "An admittedly selective visual record.",
        "feeling": "A beautifully illustrated travel journal.",
        "annotation": "Not all of these are travel recommendations.",
        "annotation_alt": "Some places are better on paper.",
        "layout": "full-bleed",
    },
    {
        "number": 5, "slug": "everything-else",
        "title": "EVERYTHING ELSE",
        "strap": "Because apparently five categories weren't enough.",
        "feeling": "A beautifully curated creative mess.",
        "annotation": "I did try to categorise these.",
        "layout": "collage",
    },
]

INTRO = {
    "heading": "I DRAW WHAT I LIKE.",
    "sub": "Which, admittedly, is quite a lot of things.",
    "lead": "Faces. Buildings. Cars.",
    "paras": [
        "Things I find beautiful. Things I find strange. Things I don't entirely understand.",
        "I've never really felt the need to choose just one.",
        "I like the idea that anything can become interesting if you look at it for long enough.",
        "So this is my little corner of the internet for collecting those things.",
    ],
    "afterthought": "Nothing more complicated than that.",
}

EYE = [
    ("01", "INTERESTING FACES",
     "There's something fascinating about the details that make a face recognisable. The expressions, the imperfections, the little features that make someone unmistakably themselves."),
    ("02", "THINGS WITH TOO MANY DETAILS",
     "Intricate mechanisms, technical drawings, complicated structures. The kind of things that make you wonder how anyone managed to put them together in the first place."),
    ("03", "OLD BUILDINGS",
     "Interesting architecture, beautiful proportions, elaborate details and places that look like they have stories to tell."),
    ("04", "BEAUTIFUL ORDINARY OBJECTS",
     "Things that most people probably wouldn't think twice about. A camera, a glass, a chair, an old book. Sometimes the most ordinary things make the most interesting subjects."),
    ("05", "THINGS I DON'T UNDERSTAND YET",
     "Because sometimes drawing something is simply an excuse to spend a little longer figuring it out."),
]

INTERVIEW = [
    ("01", "HOW WOULD YOU DESCRIBE YOUR ARTISTIC STYLE?", [
        "I've never really known how to answer this question.",
        "I like realism, but I also love the freedom of making something a little less perfect. Sometimes I want to capture every tiny detail, and other times I'm more interested in the feeling of a piece than how accurately I've drawn it.",
        "I think my style changes depending on what I'm creating, which probably isn't the most helpful answer.",
        "But I quite like it that way."], "I quite like it that way."),
    ("02", "WHAT DO YOU ENJOY DRAWING MOST?", [
        "I don't think I have a favourite subject.",
        "I'm drawn to anything that makes me want to look a little closer. Sometimes that's a face, sometimes it's the structure of a building, and sometimes it's something completely ordinary that I've decided deserves far more attention than it probably does.",
        "I think that's what I enjoy most about drawing. There doesn't have to be a particularly good reason to make something.",
        "Sometimes you just want to."], None),
    ("03", "WHERE DO YOU FIND INSPIRATION?", [
        "Pretty much everywhere, which sounds like a terribly predictable answer, but it's true.",
        "I love noticing little details. The way light falls across something, the proportions of a building, an interesting expression, or the intricacy of something mechanical.",
        "I think inspiration is less about actively searching for something extraordinary and more about paying attention to what's already there.",
        "Although occasionally, I do just see something and think, that would make a really good drawing."], None),
    ("04", "WHAT'S YOUR FAVOURITE PART OF THE CREATIVE PROCESS?", [
        "That moment when a piece starts to come together.",
        "There's usually a point where I've spent ages working on individual details, and then suddenly I take a step back and realise it's beginning to look like what I imagined.",
        "I love that feeling.",
        "Of course, there's also the slightly less enjoyable moment when I realise I've spent an unreasonable amount of time perfecting something nobody else will probably notice.",
        "But I suppose that's part of it."], None),
    ("05", "DO YOU HAVE A PARTICULAR CREATIVE PROCESS?", [
        "Not really, and I'm not entirely sure I'd want one.",
        "Some ideas sit in my head for ages before I do anything with them. Others make it onto paper almost immediately.",
        "Sometimes I know exactly what I want to create. Other times I start with a vague idea and see where it takes me.",
        "I like having the freedom to approach each piece differently.",
        "It keeps things interesting."], None),
    ("06", "WHAT DO YOU HOPE PEOPLE TAKE AWAY FROM YOUR WORK?", [
        "I'd love for someone to look at something I've created and notice a detail they might otherwise have overlooked.",
        "I don't think every piece needs to have some enormous hidden meaning or make a profound statement.",
        "Sometimes it's enough for something to be interesting, beautiful, unusual, or simply worth looking at for a little longer.",
        "And if it makes someone curious about something they hadn't thought much about before, even better."], None),
    ("07", "WHAT'S NEXT?", [
        "Your guess is as good as mine.",
        "I always seem to have more ideas than I have time to make them, and the list keeps getting longer.",
        "There are things I want to experiment with, subjects I haven't explored yet, and probably a few ideas that won't make much sense until I actually try them.",
        "I quite like not knowing exactly where it's all going.",
        "It means there's always something new to make."], None),
]

LETTER = {
    "label": "A PERSONAL NOTE FROM SARA, WITH LOVE",
    "title": "A little note from me to you.",
    "paras": [
        "I'm not entirely sure what brought you here, but I'm very glad you found your way.",
        "I've always liked the idea of having somewhere to collect the things I create. Not necessarily because they all belong together, or because there's some grand idea behind them, but simply because they each meant something to me at the time.",
        "Some pieces take hours of careful thought. Others begin with a passing interest that somehow turns into an entire afternoon spent drawing.",
        "I suppose that's what I love about making art. You never really know what will catch your attention next.",
        "This little space is my way of keeping track of it all. The finished pieces, the experiments, the ideas that worked, and the ones that perhaps needed a little more thought.",
        "I hope you enjoy looking through it as much as I've enjoyed putting it together.",
        "And if nothing else, I hope you find something that makes you stop and look twice.",
        "Thank you for being here.",
    ],
    "signoff": "Love,",
}

NOTE_KINDS = [
    ("OBSERVATIONS", "Things I've noticed."),
    ("CURRENT FIXATIONS", "Things I can't stop thinking about."),
    ("LITTLE DISCOVERIES", "Things I learned along the way."),
    ("NOTES TO SELF", "Things I probably needed reminding of."),
    ("INSPIRATION FILES", "Things worth keeping."),
]

NOTES = [
    {
        "number": 1, "slug": "on-having-no-particular-style", "kind": "THOUGHTS", "date": "OCTOBER 2026",
        "title": "ON HAVING NO PARTICULAR STYLE.", "featured": True, "image": "SA-014",
        "paras": [
            "I've been told that artists are supposed to find their style.",
            "I'm not entirely sure I've found mine.",
            "I like too many things, change my mind too often, and get distracted by whatever happens to interest me that week.",
            "Maybe that's a style in itself.",
        ],
    },
    {
        "number": 2, "slug": "on-looking-up", "kind": "OBSERVATIONS", "date": "OCTOBER 2026",
        "title": "ON LOOKING UP.", "image": "SA-010", "size": "large",
        "paras": [
            "I've noticed that I spend a surprising amount of time looking at buildings.",
            "Not necessarily the famous ones. Sometimes it's just a particularly interesting window, an unusual staircase, or a bit of architecture that someone clearly put a lot of thought into.",
            "I wonder how many interesting things we walk past every day without really noticing.",
        ],
    },
    {
        "number": 3, "slug": "on-having-too-many-ideas", "kind": "THOUGHTS", "date": "OCTOBER 2026",
        "title": "ON HAVING TOO MANY IDEAS.", "image": "SA-011", "size": "small",
        "paras": [
            "I have an ever-growing list of things I'd like to draw.",
            "Unfortunately, the list seems to grow considerably faster than my ability to actually draw them.",
            "An ongoing logistical issue.",
        ],
        "postscript": "Update: the list has gotten longer.",
        "margin": "Must get round to this.",
    },
    {
        "number": 4, "slug": "on-the-art-of-noticing", "kind": "OBSERVATIONS", "date": "SEPTEMBER 2026",
        "title": "ON THE ART OF NOTICING.", "size": "text",
        "paras": [
            "There's something quite satisfying about finding beauty in something completely ordinary.",
            "An interesting shadow. The shape of a staircase. The way someone's expression changes when they're thinking.",
            "I like the idea that the world is full of things worth looking at, if you're willing to pay attention.",
        ],
    },
    {
        "number": 5, "slug": "currently-obsessed-with-old-cars", "kind": "CURRENT FIXATIONS", "date": "SEPTEMBER 2026",
        "title": "CURRENTLY OBSESSED WITH: OLD CARS.", "image": "SA-013", "size": "large", "gallery": ["SA-011", "SA-015"],
        "paras": [
            "This month it's the engineering of old cars. The grille of a '65 Mustang, the way a racing car is really just a set of decisions about where air should go.",
            "I've been drawing the details rather than the whole thing. A headlight here, a wing mirror there.",
            "Next month it will probably be Gothic architecture. Or human anatomy. Or something completely unrelated.",
        ],
    },
    {
        "number": 6, "slug": "a-little-something-about-cathedrals", "kind": "LITTLE DISCOVERIES", "date": "AUGUST 2026",
        "title": "A LITTLE SOMETHING ABOUT CATHEDRALS.", "image": "SA-022", "size": "small",
        "paras": [
            "The dome of St Paul's is actually three domes. The one you see from outside, the one you see from inside, and a brick cone in between holding the whole thing up.",
            "Nobody mentions the cone. I think about the cone a lot.",
        ],
        "margin": "Still haven't drawn the cone.",
    },
    {
        "number": 7, "slug": "on-perfectionism", "kind": "NOTES TO SELF", "date": "AUGUST 2026",
        "title": "ON PERFECTIONISM.", "size": "text",
        "paras": [
            "At some point, you have to decide whether you're improving something or simply refusing to call it finished.",
            "I'm still working on that distinction.",
        ],
    },
    {
        "number": 8, "slug": "inspiration-file-003-the-colour-burgundy", "kind": "INSPIRATION FILES", "date": "JULY 2026",
        "title": "INSPIRATION FILE NO. 003 — THE COLOUR BURGUNDY.", "image": "SA-028", "size": "large",
        "gallery": ["SA-007", "SA-016", "SA-029"],
        "paras": [
            "A collection of things that are the right sort of red. Dark enough to be serious. Warm enough not to be.",
        ],
    },
    {
        "number": 9, "slug": "on-knowing-when-to-stop", "kind": "THOUGHTS", "date": "OCTOBER 2026",
        "title": "ON KNOWING WHEN TO STOP.", "image": "SA-001", "size": "small",
        "paras": [
            "The Westminster painting on the cover isn't finished. I decided it was, which is a different thing.",
            "There's a version of it in my head with the whole bridge painted in. I think it's worse.",
        ],
        "postscript": "Still haven't started this.",
    },
]

ENQUIRIES = {
    "strap": "For something that doesn't exist yet.",
    "corner": "ORIGINAL WORKS & PRIVATE COMMISSIONS",
    "manifesto_heading": ["MADE ONCE.", "KEPT FOREVER."],
    "manifesto": [
        "I don't make prints, reproductions or editions.",
        "Every piece I create is an original. Made by hand, made with intention, and made only once.",
        "I like the idea that a painting can belong entirely to one person. That somewhere, in someone's home, there's a piece of art that exists nowhere else in the world.",
        "No duplicates. No second versions. No one else with the same thing hanging on their wall.",
        "Just one piece, created for one place, to become part of someone's life.",
        "And I think there's something rather lovely about that.",
    ],
    "commissions_heading": "SOMETHING ENTIRELY YOUR OWN.",
    "commissions_sub": "Original artwork, made especially for you.",
    "commissions": [
        "I occasionally take on private commissions.",
        "Whether it's a portrait, a place, an object, or something a little harder to categorise, I'm always interested in hearing about ideas that someone would like to bring to life.",
        "I don't work from a fixed catalogue, and I don't offer reproductions of existing pieces.",
        "Every commission begins with a conversation and becomes an original artwork, created specifically for the person who will own it.",
        "I work on a larger scale, allowing each piece the space and attention it deserves.",
        "If you have something in mind, I'd love to hear about it.",
    ],
    "commissions_tags": ["ORIGINAL ARTWORK ONLY", "ONE OF ONE", "LARGE-FORMAT PIECES", "BY PRIVATE COMMISSION"],
    "process": [
        ("I.", "THE IDEA", "Tell me what you're imagining.", [
            "It doesn't need to be perfectly formed.",
            "You might have a particular subject in mind, a reference photograph, a space you'd like to fill, or simply an idea you've been thinking about.",
            "Tell me a little about it, and we'll see where it goes."]),
        ("II.", "THE CONVERSATION", "Let's work out the details.", [
            "We'll discuss the subject, scale, medium, creative direction and any practical considerations.",
            "I'll let you know whether it's something I can take on, along with the proposed price and timeframe."]),
        ("III.", "THE PIECE", "Made once. Just for you.", [
            "Once we've agreed on the direction, I'll begin creating your original artwork.",
            "The finished piece will be yours alone.",
            "No prints. No reproductions. No second editions.",
            "Just the original."]),
    ],
    "form_heading": "SHALL WE MAKE SOMETHING?",
    "form_sub": ["Have an idea? A particular subject? An empty wall that's been bothering you?", "Tell me about it."],
    "fields": [
        ("name", "YOUR NAME", "What should I call you?", "text"),
        ("email", "EMAIL ADDRESS", "Somewhere I can find you", "email"),
        ("idea", "WHAT ARE YOU THINKING?", "Tell me about your idea...", "textarea"),
        ("size", "APPROXIMATE SIZE", "Do you have a size in mind?", "text"),
        ("timeline", "TIMELINE", "Is there a particular date you're working towards?", "text"),
        ("references", "REFERENCE IMAGES", "Have something to show me? (Optional)", "file"),
    ],
    "form_button": "SEND YOUR ENQUIRY",
    "form_footnote": "No need to have it all figured out. That's what the conversation is for.",
    "pricing": "Commissions are individually priced according to scale and complexity.",
    "note_title": "A NOTE ON ORIGINALS.",
    "note": [
        "I think there's something special about owning something that nobody else has.",
        "Not because it's expensive, or rare, or particularly important in the grand scheme of things.",
        "But because it's yours.",
        "I love the thought of creating a piece that eventually finds its place in someone's home. Something that becomes part of their everyday life. Something they walk past every morning, notice in different lights, and perhaps grow a little more attached to over time.",
        "And I love knowing that there won't be another one quite like it.",
        "I don't want to make hundreds of the same thing.",
        "I'd rather make one thing, really well, for someone who genuinely loves it.",
        "That's the idea, anyway.",
    ],
    "closing": ["SOMETHING WORTH KEEPING.", "Made once. Made for you."],
}
