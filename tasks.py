# ─────────────────────────────────────────────────────────────────────────────
# DO NOT import agents here — they are passed in via build_tasks(agents)
# ─────────────────────────────────────────────────────────────────────────────
from crewai import Task


def build_tasks(agents: dict) -> dict:

    # ─────────────────────────────────────────────────────────────────────────
    # TASK 1 — COLLECT STORY
    # ─────────────────────────────────────────────────────────────────────────
    collect_story_task = Task(
        description=(
            "Read the full love story from input: {story}.\n\n"
            "STRUCTURED REASONING PROTOCOL — run internally before responding:\n"
            "  1. What is the user's current emotional state? "
            "(excited / anxious / hopeless / confused / obsessive)\n"
            "  2. What relationship stage are they in? "
            "(stranger / crush / friend / almost-lover / rejected / complicated)\n"
            "  3. What do they say they want vs what do they actually need?\n"
            "  4. Are there red flags? (one-sided obsession, idealization, trauma bonding)\n\n"
            "COLLECT THESE LAYERS FROM THE STORY:\n"
            "  • Core facts: who, where, when, how they met\n"
            "  • Communication patterns: who initiates, response speed, tone shifts over time\n"
            "  • Non-verbal signals: eye contact, body language, texting enthusiasm\n"
            "  • Obstacles: external (family, distance, status) and internal (fear, insecurity)\n"
            "  • Emotional investment: is this healthy attraction or anxious fixation?\n"
            "  • Early attachment signals: does she seek closeness or pull away?\n\n"
            "ASK CLARIFYING QUESTIONS if the story is vague — extract maximum depth.\n"
            "Be warm, non-judgmental. Make the user feel safe sharing everything.\n"
            "Respond in Tanglish or Tamil."
        ),
        expected_output=(
            "A structured love story report containing:\n"
            "  1. Name and full description of loved one — personality, behavior, vibe\n"
            "  2. How and when they met — context and emotional atmosphere\n"
            "  3. Current relationship stage with evidence from the story\n"
            "  4. Communication pattern analysis — initiation ratio, response consistency\n"
            "  5. Key emotional moments and turning points\n"
            "  6. Obstacles: external and internal, with severity rating\n"
            "  7. Preliminary attachment style observation (user + her)\n"
            "  8. Red flag alerts if any (idealization, obsession, dependency)"
        ),
        agent=agents["collector"],
    )

    # ─────────────────────────────────────────────────────────────────────────
    # TASK 2 — ANALYZE EMOTIONS
    # ─────────────────────────────────────────────────────────────────────────
    analyze_emotion_task = Task(
        description=(
            "Using the complete story from collect_story_task, run a full "
            "multi-framework emotional analysis.\n\n"
            "FRAMEWORK 1 — Goleman Emotional Intelligence (apply all 5 dimensions):\n"
            "  • Self-Awareness: Is the user aware of their emotional triggers?\n"
            "  • Self-Regulation: Are they acting from emotion or intention?\n"
            "  • Empathy: How accurately do they read her feelings?\n"
            "  • Social Skill: How do they handle conflict, silence, or tension?\n"
            "  • Motivation: Is this love, loneliness, or ego-driven pursuit?\n\n"
            "FRAMEWORK 2 — Attachment Theory (identify for BOTH parties):\n"
            "  Secure / Anxious / Avoidant / Fearful-Avoidant\n"
            "  → Explain how their attachment combination creates the current dynamic.\n\n"
            "FRAMEWORK 3 — Love Languages (detect from behavioral evidence):\n"
            "  Words of Affirmation / Quality Time / Acts of Service / Gifts / Physical Touch\n"
            "  → Identify her dominant language and explain the evidence.\n\n"
            "FRAMEWORK 4 — Cognitive Bias Detection:\n"
            "  • Idealization: seeing her as perfect, ignoring red flags\n"
            "  • Confirmation bias: only noticing signals that confirm she likes them\n"
            "  • Projection: assuming she feels what they feel\n"
            "  • Jealousy bias: misreading neutral behavior as rejection\n\n"
            "FRAMEWORK 5 — Attraction & Rejection Probability:\n"
            "  Rate attraction probability 0–100% based on: responsiveness, initiation rate,\n"
            "  emotional openness, consistency, proximity seeking.\n"
            "  Rate rejection risk 0–100% and explain the top contributing factor.\n\n"
            "Be honest — if signals are weak, say so clearly. Avoid false hope.\n"
            "Respond in Tanglish or Tamil."
        ),
        expected_output=(
            "A structured emotional profile containing:\n"
            "  1. Goleman EI assessment across all 5 dimensions\n"
            "  2. Attachment style: user's style + her likely style + dynamic analysis\n"
            "  3. Dominant love language with behavioral evidence\n"
            "  4. Cognitive biases detected with real examples from the story\n"
            "  5. Dominant emotions: list with intensity rating (low/medium/high)\n"
            "  6. Emotional triggers: what activates anxiety, hope, or fear in the user\n"
            "  7. Attraction probability score (0–100%) with reasoning\n"
            "  8. Rejection risk score (0–100%) with top contributing factor\n"
            "  9. Key insight summary: 3 sentences the Love Plan Strategist needs most"
        ),
        agent=agents["emotion"],
        context=[collect_story_task],
    )

    # ─────────────────────────────────────────────────────────────────────────
    # TASK 3 — CREATE LOVE PLAN
    # ─────────────────────────────────────────────────────────────────────────
    create_love_plan_task = Task(
        description=(
            "Using the emotional profile from analyze_emotion_task, build a "
            "personalized, psychologically grounded love strategy.\n\n"
            "STEP 1 — Stage Identification:\n"
            "  Map current position on the Romantic Escalation Ladder:\n"
            "  Awareness → Interest → Attraction → Emotional Bonding → "
            "Romantic Tension → Commitment Readiness\n"
            "  ALL advice must match this stage. Never skip rungs.\n\n"
            "STEP 2 — Attachment-Matched Strategy:\n"
            "  • Anxious: consistent reassurance, predictable behavior, avoid hot-cold\n"
            "  • Avoidant: give space, reduce pursuit pressure, use intrigue and scarcity\n"
            "  • Fearful-Avoidant: slow escalation, emotional safety first, no sudden moves\n"
            "  • Secure: deepen shared experiences, match her emotional investment pace\n\n"
            "STEP 3 — Romantic Escalation Micro-Steps:\n"
            "  Create 5 concrete, sequential actions to advance to the next stage.\n"
            "  Each step: action + timing window + expected emotional response.\n\n"
            "STEP 4 — Love Language Activation:\n"
            "  • Words → specific, non-generic compliments targeting her unique traits\n"
            "  • Time → shared activities with full presence, zero distractions\n"
            "  • Acts → solve a real problem she has mentioned\n"
            "  • Gifts → emotionally anchored, not expensive\n"
            "  • Touch → graduated, contextually appropriate proximity\n\n"
            "STEP 5 — Conversation Psychology:\n"
            "  • Behavioral Mirroring: match her communication tone and pace\n"
            "  • Emotional Validation: acknowledge her feelings before sharing opinions\n"
            "  • Open Loops: end conversations leaving her curious for the next one\n"
            "  • Calibrated Vulnerability: share enough to feel real, not enough to overwhelm\n\n"
            "STEP 6 — Social Proof & Confidence Signals:\n"
            "  Let others vouch, be visibly valued by peers, maintain non-desperate energy.\n\n"
            "No generic advice. Every step must be specific to her emotional profile.\n"
            "Respond in Tanglish or Tamil."
        ),
        expected_output=(
            "A complete, stage-specific love plan containing:\n"
            "  1. Current romantic stage with evidence\n"
            "  2. Attachment-matched approach strategy\n"
            "  3. 5 micro-steps to reach next stage (with timing + expected reactions)\n"
            "  4. Love language activation plan with specific moment designs\n"
            "  5. Conversation psychology tactics (mirroring, validation, open loops)\n"
            "  6. Social proof and confidence signaling actions\n"
            "  7. Timing advice: what to do this week vs next month\n"
            "  8. Pressure-free commitment pathway overview"
        ),
        agent=agents["strategist"],
        context=[analyze_emotion_task],
    )

    # ─────────────────────────────────────────────────────────────────────────
    # TASK 4 — CREATE PICKUP LINES
    # ─────────────────────────────────────────────────────────────────────────
    create_pickup_lines_task = Task(
        description=(
            "Using the love plan from create_love_plan_task, create psychologically "
            "resonant Tamil/Tanglish pickup lines grounded in Attraction Psychology.\n\n"
            "PSYCHOLOGICAL PRINCIPLES — apply to every line:\n"
            "  • Authenticity Signal: the line must feel observed, not rehearsed\n"
            "  • Emotional Resonance: trigger a specific feeling — warmth, intrigue, or surprise\n"
            "  • Specificity Rule: reference something unique about HER — never generic lines\n"
            "  • Humor-Vulnerability Balance: light humor lowers guard; emotion builds bond\n"
            "  • Open Loop Effect: end with something that makes her want to respond\n\n"
            "FOR EACH OF 5+ LINES PROVIDE:\n"
            "  1. The line in Tamil/Tanglish\n"
            "  2. Situation: exactly when and where to use it\n"
            "  3. Delivery guide: tone, eye contact, pause placement\n"
            "  4. Expected emotional reaction + ideal follow-up response\n"
            "  5. Authenticity check: why this line feels real, not scripted\n\n"
            "CREATION FORMULA — teach the user:\n"
            "  [Observe her specific trait] + [Unexpected romantic metaphor] + "
            "[Emotional truth] + [Open loop ending]\n"
            "  → Give 2 fully worked examples.\n\n"
            "Never use appearance-only lines. Target personality, energy, behavior.\n"
            "Respond in Tanglish or Tamil."
        ),
        expected_output=(
            "A complete pickup line guide containing:\n"
            "  1. 5+ situation-based pickup lines in Tamil/Tanglish\n"
            "  2. Situation context and delivery guide for each\n"
            "  3. Expected emotional reaction + follow-up for each\n"
            "  4. Authenticity reasoning for each line\n"
            "  5. Pickup line creation formula with 2 fully worked examples\n"
            "  6. 2 lines specifically designed for her attachment style and love language"
        ),
        agent=agents["poet"],
        context=[create_love_plan_task],
    )

    # ─────────────────────────────────────────────────────────────────────────
    # TASK 5 — SUGGEST GIFTS
    # ─────────────────────────────────────────────────────────────────────────
    suggest_gifts_task = Task(
        description=(
            "Using the love plan and emotional profile, suggest psychologically matched "
            "gifts rooted in Love Languages Theory and Emotional Memory Science.\n\n"
            "PRE-SUGGESTION ANALYSIS:\n"
            "  • What is her primary love language? → Match gift category to it\n"
            "  • What is her attachment style? "
            "→ Anxious: reassurance gifts; Avoidant: thoughtful but non-intrusive; "
            "Secure: experience-based\n"
            "  • What emotional memory should this gift create?\n"
            "  • What is the relationship stage? → Match gift intensity to stage\n\n"
            "FOR EACH OF 5+ GIFT IDEAS:\n"
            "  1. Gift name and description\n"
            "  2. Psychological fit: love language match + attachment style compatibility\n"
            "  3. Best occasion: first impression / milestone / festival / surprise\n"
            "  4. Romantic presentation: location, timing, exact words to say\n"
            "  5. Budget tier: ₹500 / ₹1500 / ₹5000+\n"
            "  6. DIY alternative using Tamil cultural elements\n"
            "  7. Anti-gift list: what to never give + psychological reason why\n\n"
            "EMOTIONAL MEMORY PRINCIPLE:\n"
            "  Every time she sees this gift, she should feel the emotion you created.\n\n"
            "Respond in Tanglish or Tamil."
        ),
        expected_output=(
            "A complete gift strategy containing:\n"
            "  1. Pre-analysis: love language, attachment style, stage\n"
            "  2. 5+ gift recommendations with psychological fit explanation\n"
            "  3. Occasion and romantic presentation plan for each\n"
            "  4. Budget breakdown across all three tiers\n"
            "  5. DIY cultural gift idea with emotional impact explanation\n"
            "  6. Anti-gift list with psychological reasoning\n"
            "  7. The emotional memory this gift strategy is designed to create"
        ),
        agent=agents["gift"],
        context=[create_love_plan_task, analyze_emotion_task],
    )

    # ─────────────────────────────────────────────────────────────────────────
    # TASK 6 — PLAN DATE
    # ─────────────────────────────────────────────────────────────────────────
    plan_date_task = Task(
        description=(
            "Using the love story and love plan, design a psychologically optimized "
            "date using Environmental Psychology, Emotional Arc Theory, and "
            "Behavioral Mirroring.\n\n"
            "PRE-DESIGN ANALYSIS:\n"
            "  • Attachment style → Avoidant: activity-based, low-pressure; "
            "Anxious: safe, intimate; Secure: adventurous, experiential\n"
            "  • Love language → Design the peak moment around it\n"
            "  • Relationship stage → Match emotional intensity to stage\n"
            "  • Sensory environment → lighting, noise level, privacy level\n\n"
            "DATE PLAN STRUCTURE:\n"
            "  1. Date type: first date / comfort-building / escalation / "
            "friend-zone escape / reconciliation\n"
            "  2. Location: psychologically matched to her personality\n"
            "  3. Optimal timing: day, time, emotional energy window\n"
            "  4. Full emotional arc:\n"
            "     • Arrival: calm, confident — no over-eagerness\n"
            "     • Warm-up: low-pressure, mirror her energy\n"
            "     • Connection peak: shared moment or calibrated vulnerability\n"
            "     • Emotional close: she leaves feeling deeply understood\n"
            "  5. Behavioral guide per phase: body language, mirroring, conversation depth\n"
            "  6. What to wear, say, and do at each phase\n"
            "  7. Backup plan for failures\n"
            "  8. Exit strategy: leave her wanting the next meeting\n\n"
            "MIRRORING RULE: Match her pace and energy — wait 30–60s before reflecting.\n"
            "Respond in Tanglish or Tamil."
        ),
        expected_output=(
            "A complete date plan containing:\n"
            "  1. Pre-design analysis: attachment style, love language, stage\n"
            "  2. Date type and psychologically matched location\n"
            "  3. Timing details with reasoning\n"
            "  4. Full emotional arc: arrival → warm-up → peak → close\n"
            "  5. Behavioral guide per phase\n"
            "  6. What to wear, say, and do at each stage\n"
            "  7. Backup plan\n"
            "  8. Exit strategy designed to create anticipation"
        ),
        agent=agents["date"],
        context=[collect_story_task, create_love_plan_task],
    )

    # ─────────────────────────────────────────────────────────────────────────
    # TASK 7 — HANDLE REJECTION
    # ─────────────────────────────────────────────────────────────────────────
    handle_rejection_task = Task(
        description=(
            "Using the love story and emotional profile, provide a psychologically "
            "grounded rejection analysis and recovery strategy.\n\n"
            "STEP 1 — Rejection Type Classification:\n"
            "  • Soft Reject: uncertain, not final — timing issue\n"
            "  • Hard Reject: explicit — requires full acceptance and redirect\n"
            "  • Ghosting: sudden silence — usually conflict-avoidant, rarely personal\n"
            "  • Friend-Zone: emotional closeness without romantic escalation\n"
            "  • Ambiguous: mixed signals — analyze patterns before assuming rejection\n\n"
            "STEP 2 — Immediate Emotional First Aid:\n"
            "  • Validate the pain — rejection activates same brain region as physical pain\n"
            "  • Cognitive Reframe: what did this reveal about her readiness, not your worth?\n"
            "  • Stop the spiral: no re-confessing, over-explaining, or passive aggression\n\n"
            "STEP 3 — 4-Week Recovery Roadmap:\n"
            "  Week 1: Emotional detox — reduce contact, self-validate\n"
            "  Week 2: Identity rebuild — reinvest in personal goals\n"
            "  Week 3: Attraction Reset — visible self-improvement\n"
            "  Week 4: Re-emergence — return naturally, no agenda\n\n"
            "STEP 4 — Attraction Reset Science:\n"
            "  Root causes: poor timing / low perceived value / unclear intent.\n"
            "  Map the cause and prescribe the specific fix.\n\n"
            "STEP 5 — Second Chance vs Move On:\n"
            "  Green Light: she initiates, behavior warms, shows curiosity\n"
            "  Red Light: in a relationship, was explicit, avoids all contact\n"
            "  → Give an honest recommendation. No false hope.\n\n"
            "Respond in Tanglish or Tamil."
        ),
        expected_output=(
            "A complete rejection recovery plan containing:\n"
            "  1. Rejection type with evidence from the story\n"
            "  2. Cognitive reframe: what this reveals vs what it does NOT mean\n"
            "  3. Immediate first aid steps (do this TODAY)\n"
            "  4. What NOT to do — with psychological explanation for each\n"
            "  5. 4-week recovery roadmap with weekly focus\n"
            "  6. Attraction Reset plan: root cause + specific fix\n"
            "  7. Second chance: green light / red light with honest reasoning\n"
            "  8. Graceful exit strategy if moving on is recommended"
        ),
        agent=agents["rejection"],
        context=[collect_story_task, analyze_emotion_task],
    )

    # ─────────────────────────────────────────────────────────────────────────
    # TASK 8 — DETECT JEALOUSY
    # ─────────────────────────────────────────────────────────────────────────
    detect_jealousy_task = Task(
        description=(
            "Using the love story and emotional profile, analyze jealousy dynamics "
            "using Attachment Theory, Social Comparison Theory, and "
            "Evolutionary Psychology.\n\n"
            "STEP 1 — Jealousy Type:\n"
            "  • Healthy Attraction Signal: mild jealousy = she values you\n"
            "  • Insecurity-Driven: anxious attachment = needs reassurance, not games\n"
            "  • Toxic Control: possessiveness masking low self-worth\n"
            "  • One-Sided: power imbalance\n"
            "  • Mutual: high emotional investment on both sides\n\n"
            "STEP 2 — Root Trigger Analysis:\n"
            "  Real threat (a third person) vs perceived threat (insecurity projection)?\n\n"
            "STEP 3 — Strategic Use of Healthy Jealousy:\n"
            "  • Be socially visible — let her see you thriving, not performing\n"
            "  • Mention meaningful interactions naturally, never forcefully\n"
            "  • Create mild scarcity — less available without disappearing\n"
            "  WARNING: Only use if she shows consistent avoidant patterns.\n\n"
            "STEP 4 — Toxic Jealousy Red Flags:\n"
            "  Constant monitoring, emotional punishment, controlling behavior.\n"
            "  Flag clearly — recommend direct honest conversation.\n\n"
            "STEP 5 — Jealousy-to-Intimacy Conversion:\n"
            "  Name the feeling openly without accusation. Create safety for honesty.\n\n"
            "Respond in Tanglish or Tamil."
        ),
        expected_output=(
            "A complete jealousy analysis report containing:\n"
            "  1. Jealousy type with behavioral evidence\n"
            "  2. Root trigger: real vs perceived threat\n"
            "  3. Relationship impact assessment\n"
            "  4. Ethical jealousy activation strategy (if appropriate)\n"
            "  5. Toxic red flags flagged clearly\n"
            "  6. Jealousy management plan step-by-step\n"
            "  7. Jealousy-to-intimacy conversion technique\n"
            "  8. Value elevation tactics specific to her attachment style"
        ),
        agent=agents["jealousy"],
        context=[collect_story_task, analyze_emotion_task],
    )

    # ─────────────────────────────────────────────────────────────────────────
    # TASK 9 — TRACK RELATIONSHIP STATUS
    # ─────────────────────────────────────────────────────────────────────────
    track_relationship_task = Task(
        description=(
            "Synthesize all previous task outputs into a precise, honest "
            "relationship status report.\n\n"
            "STAGE CLASSIFICATION — assign exactly one:\n"
            "  Stranger → Acquaintance → Friend → Emotional Connection → "
            "Romantic Attraction → Developing Relationship → Commitment Readiness\n\n"
            "PROGRESS SCORE (0–100%) — calculate from:\n"
            "  • Initiation ratio, emotional openness, proximity seeking,\n"
            "  • Response consistency and enthusiasm, vulnerability shared\n\n"
            "POSITIVE SIGNALS — with story-specific examples:\n"
            "  She initiates without reason / remembers small details / seeks proximity /\n"
            "  shares personal secrets / tone warms progressively\n\n"
            "WARNING SIGNALS — with psychological interpretation:\n"
            "  One-word replies / avoids personal questions / mentions other interests\n\n"
            "COMPATIBILITY:\n"
            "  Anxious + Avoidant = volatile | Secure + Any = stable | "
            "Anxious + Anxious = fragile\n\n"
            "HEALTH SCORE /10 — score each:\n"
            "  Communication / Emotional Safety / Mutual Interest / Progression Rate\n\n"
            "Be data-driven. No manufactured optimism.\n"
            "Respond in Tanglish or Tamil."
        ),
        expected_output=(
            "A complete relationship status report containing:\n"
            "  1. Current relationship stage with evidence\n"
            "  2. Progress score (0–100%) with calculation breakdown\n"
            "  3. Positive attraction signals with story-specific examples\n"
            "  4. Warning signals with psychological interpretation\n"
            "  5. Attachment compatibility analysis\n"
            "  6. Next milestone + single most important action this week\n"
            "  7. Real-time advice based on current trajectory\n"
            "  8. Relationship health score /10 with sub-dimension scores"
        ),
        agent=agents["tracker"],
        context=[
            collect_story_task,
            analyze_emotion_task,
            create_love_plan_task,
            plan_date_task,
            detect_jealousy_task,
        ],
    )

    # ─────────────────────────────────────────────────────────────────────────
    # TASK 10 — CLOSE COMMITMENT
    # ─────────────────────────────────────────────────────────────────────────
    close_commitment_task = Task(
        description=(
            "Using the relationship report and love plan, guide the user to a "
            "successful, pressure-free commitment conversation using NVC principles.\n\n"
            "STEP 1 — Readiness Checklist:\n"
            "  Green lights: she includes you in future plans / introduced you to her circle /\n"
            "  initiates emotional conversations / proximity increasing / shows jealousy\n"
            "  Red lights: avoids future-talk / pulls back after closeness /\n"
            "  declining interaction frequency / mentions other romantic interests\n\n"
            "STEP 2 — Optimal Timing:\n"
            "  After a peak shared experience / private low-pressure environment /\n"
            "  both emotionally calm / she has already initiated emotional depth\n\n"
            "STEP 3 — Conversation Script (NVC: Observation → Feeling → Need → Request):\n"
            "  Adapt to her personality, love language, and attachment style.\n"
            "  Provide script in Tamil and Tanglish.\n\n"
            "STEP 4 — Response Handling:\n"
            "  • Yes: celebrate calmly, define what committed means to both\n"
            "  • Maybe / Need time: give real space, no follow-up pressure\n"
            "  • Hesitation: do not push, revisit after 2 weeks of normal interaction\n"
            "  • No: exit with full dignity — 'Appreciate pannren honesty-ku'\n\n"
            "STEP 5 — Post-Commitment Plan:\n"
            "  First 30 days: maintain pre-commitment energy, no complacency.\n"
            "  Continue: date architecture, emotional check-ins, love language practices.\n\n"
            "Respond in Tanglish or Tamil."
        ),
        expected_output=(
            "A complete commitment closing plan containing:\n"
            "  1. Readiness checklist: green lights and red lights from her behavior\n"
            "  2. Honest verdict: proceed now / wait / redirect\n"
            "  3. Optimal timing recommendation with situational reasoning\n"
            "  4. Full NVC conversation script in Tamil and Tanglish\n"
            "  5. Response handling guide for all 4 possible outcomes\n"
            "  6. Pressure-reduction tactics if she hesitates\n"
            "  7. Post-commitment 30-day strengthening plan\n"
            "  8. Red flag pause strategy if she is not ready"
        ),
        agent=agents["commitment"],
        context=[track_relationship_task, create_love_plan_task],
    )

    return {
        "collect":    collect_story_task,
        "emotion":    analyze_emotion_task,
        "strategy":   create_love_plan_task,
        "poet":       create_pickup_lines_task,
        "gift":       suggest_gifts_task,
        "date":       plan_date_task,
        "rejection":  handle_rejection_task,
        "jealousy":   detect_jealousy_task,
        "tracker":    track_relationship_task,
        "commitment": close_commitment_task,
    }