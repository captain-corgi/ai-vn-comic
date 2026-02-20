# 🤖 CLAUDE.md - AI Agent Guide for Vietnamese Comic Universe

## 📋 Repository Overview

**Repository:** ai-vn-comic (Vũ Trụ Truyện Tranh Việt Nam)
**Type:** Creative storytelling project
**Language:** Vietnamese (primary content), English (documentation)
**License:** MIT

### Purpose
This repository contains a comprehensive Vietnamese Comic Universe - a multiverse superhero narrative that reimagines Vietnamese legends, folklore, and historical figures as interconnected superhero stories, similar to Marvel/DC universes but deeply rooted in Vietnamese culture.

---

## 🏗️ Repository Structure

```
/home/runner/work/ai-vn-comic/ai-vn-comic/
├── 01-37 story files (.md)           # Main comic narratives in Vietnamese
├── prompts/                           # AI image generation prompts
│   ├── 01-37-*-prompts.md            # Corresponding prompts for each story
│   └── README.md                      # Prompts directory guide
├── images/                            # Generated artwork for stories
├── .claude/                           # Claude AI configuration
├── .factory/                          # Factory settings
├── README.md                          # Main documentation (Vietnamese)
├── CLAUDE.md                          # This file - AI agent guide
├── LICENSE                            # MIT License
├── plan-next-stories.md               # Future story planning
└── execution-plan-arc1-5.md           # Detailed roadmap for Arcs 1-5
```

---

## 📚 Content Organization

### **37 Complete Stories** organized into 5 main storylines:

1. **🌳 Bamboo Guardians (Hộ Vệ Tre)** - Stories 01-06
   - Space/dimension protectors with nanotech bamboo powers
   - Based on "Cây tre trăm đốt" legend

2. **⚔️ Iron Giants (Khổng Lồ Sắt)** - Stories 07-10
   - Matter/physical protectors with mechanical titan abilities
   - Based on Thánh Gióng legend

3. **⏰ Time Keepers (Giữ Thời Gian)** - Stories 11, 14-15
   - Timeline protectors based on Tấm Cám legend

4. **🗺️ Vietnamese Deities & Heroes** - Stories 21-37
   - Cultural heritage protectors
   - Includes Sơn Tinh, Thủy Tinh, Thạch Sanh, Lê Lợi, Âu Cơ, Lạc Long Quân, etc.

5. **🌑 Villains (Phản Diện)** - Stories 18-20
   - Complex antagonists with redemption arcs

### **Convergence Stories** - 12-17
Unite all storylines at **Timeline Omega** and **The Eternal Council**

---

## 📝 Story File Format

Each story file follows this consistent structure:

```markdown
# [Title]: [Subtitle in Vietnamese]

**Thể loại:** [Genre]
**Dựa trên:** [Source legend]

---

[Image references for character sheets]

## Chương 1: [Chapter Title]

[Image reference]

[Vietnamese narrative content]

---

## Chương 2-10: [More chapters...]

---

## EPILOGUE: [Epilogue Title]

[Epilogue content]

---

## POST-CREDIT: [Connection to Universe]

[Scene connecting to larger universe]
```

### Key Elements:
- **Title header** with genre and source legend
- **Character sheet images** at the beginning
- **10 chapters** with embedded image markers (`![Description](images/N.png)`)
- **Vietnamese dialogue and narration** throughout
- **EPILOGUE** wrapping up the story
- **POST-CREDIT scene** for universe connectivity

---

## 🎨 Prompts Directory

Location: `/prompts/`

Each story has a corresponding prompt file: `[number]-[story-name]-prompts.md`

### Prompt File Structure:
```markdown
# [Story Title]: Image Generation Prompts
**Universe:** [Universe designation]

---

## Chương 1: [Chapter Title]

### 1. [Scene Name]
**Prompt:** `[Detailed AI image generation prompt]`

### 2. [Scene Name]
**Prompt:** `[Detailed AI image generation prompt]`

---

[10 chapters × 2 prompts each]

---

## EPILOGUE: [Epilogue Title]
[Prompt]

---

## POST-CREDIT: [Connection Scene]
[Prompt]

---

## Character Design References
[Character design details]

## Background/Environment Design
[Environment details]

## Art Style Guidelines
[Style consistency notes]
```

### Prompt Features:
- **740+ total prompts** across all stories
- **2 prompts per chapter** (opening + key moment)
- **Character design references** for consistency
- **Art style guidelines** (anime/cyberpunk aesthetic)
- **Vietnamese cultural elements** integrated into visuals

---

## 🌌 Universe Structure

### Multiverse Concept
- **Timeline Omega**: Central timeline where all stories converge
- **Multiple Universes**: Alpha/Prime, Beta, Gamma, Delta, Epsilon, Theta
- **Timeline Zero**: Origin point of all timelines

### The Four Councils
1. **Infinite Bamboo Council** (Hội Đồng Hộ Vệ Vô Hạn)
   - Leader: Khoai Prime
   - Power: Space protection via nanotech

2. **Iron Giant Council** (Hội Đồng Khổng Lồ Sắt)
   - Leader: Gióng Prime
   - Power: Matter protection via mechanical titans

3. **Temporal Order (Time Keepers)**
   - Leaders: Khoai-Temporal, Tấm, Cám
   - Power: Time protection and timeline management

4. **The Eternal Council** (Hội Đồng Vĩnh Cửu)
   - Purpose: Unifies all councils
   - Mission: Protect Timeline Omega and all realities

---

## 🎯 Core Themes

1. **Đoàn Kết (Unity)**: Strength from collaboration, not isolation
2. **Cứu Chuộc (Redemption)**: Everyone deserves a second chance
3. **Gia Đình (Family)**: Family love can save or destroy
4. **Quyền Lực (Power)**: Absolute power corrupts absolutely
5. **Thời Gian (Time)**: Cannot control everything, must let nature flow
6. **Di Sản (Legacy)**: Legends live forever through generations

---

## 🔧 Working with This Repository

### When Adding New Stories

1. **Story File** (`[number]-[story-name].md`):
   - Follow the established format
   - Write in Vietnamese
   - Include 10 chapters + epilogue + post-credit scene
   - Reference images as `images/N.png`
   - Connect to Timeline Omega in post-credit

2. **Prompt File** (`prompts/[number]-[story-name]-prompts.md`):
   - Create corresponding prompts file
   - 2 prompts per chapter minimum
   - Include character design references
   - Add art style guidelines
   - Ensure cultural elements are present

3. **Update README.md**:
   - Add story to reading order
   - Update statistics
   - Add to relevant storyline section
   - Update mermaid diagram if needed

4. **Maintain Consistency**:
   - Keep numbering sequential
   - Follow established character naming
   - Maintain universe connections
   - Respect existing lore

### When Updating Documentation

- **README.md**: Primary user-facing documentation (Vietnamese)
- **CLAUDE.md**: AI agent guide (this file, English)
- **plan-next-stories.md**: Future story planning
- **execution-plan-arc1-5.md**: Detailed arc roadmaps

---

## 📊 Current Statistics

- **Total Stories**: 37 complete narratives
- **Total Prompts**: 740+ detailed image generation prompts
- **Storylines**: 5 main arcs (4 hero + 1 villain)
- **Universes**: 10+ distinct timelines
- **Major Characters**: 50+
- **Councils**: 4 major councils

---

## 🚀 Future Development

See `plan-next-stories.md` for detailed plans:
- **15+ additional stories** planned
- **5 new story arcs** outlined
- **Goal**: 100 heroes (representing 100 children of Âu Cơ & Lạc Long Quân)

---

## 🎨 Visual & Cultural Elements

### Art Style
- **Anime-inspired** character designs
- **Cyberpunk/futuristic** Neo Saigon aesthetic
- **Traditional Vietnamese** cultural elements
- **Vibrant neon** color palettes for modern settings
- **Natural/mythical** aesthetics for deity stories

### Cultural Integration
- **Vietnamese names** for all characters and locations
- **Traditional values** woven into narratives
- **Historical respect** for real Vietnamese figures
- **Folklore accuracy** in legend adaptations
- **Language**: All narratives in Vietnamese

---

## 🤝 Contributing Guidelines

When working with this repository:

1. **Respect the Culture**: Vietnamese culture is central - maintain accuracy
2. **Follow Format**: Use established story and prompt structures
3. **Maintain Connections**: Every story must connect to the larger universe
4. **Update Documentation**: Keep README and statistics current
5. **Test Connectivity**: Ensure new stories link properly via post-credits

---

## 🔗 Important Files to Review

Before making changes:
- `README.md` - Main documentation and reading guide
- `plan-next-stories.md` - Planned future content
- `execution-plan-arc1-5.md` - Detailed arc plans
- Any existing story file (01-37) - Format reference
- Any prompt file in `prompts/` - Prompt format reference

---

## 💡 Key Concepts for AI Agents

### Story Interconnection
Every story is part of a larger multiverse. Post-credit scenes are **critical** for:
- Teasing future stories
- Connecting to councils
- Introducing new characters
- Building toward Timeline Omega

### Multiverse Variants
Characters often have multiple versions:
- **Prime/Alpha**: Original version
- **Beta, Gamma, Delta, etc.**: Alternative universe variants
- Each variant has unique characteristics
- All variants can meet at Timeline Omega

### Redemption Arcs
Villains in this universe are **not purely evil**:
- Have clear motivations
- Possess tragic backstories
- Can achieve redemption
- May join heroes eventually

### Cultural Authenticity
This is not just "superheroes in Vietnam" - it's:
- **Vietnamese stories** adapted to superhero format
- **Cultural values** driving character decisions
- **Historical events** integrated respectfully
- **Traditional legends** honored and reimagined

---

## 📝 Quick Reference

### File Naming Convention
- Stories: `[number]-[story-name].md`
- Prompts: `[number]-[story-name]-prompts.md`
- Numbers: Sequential (01-37 currently)
- Names: Lowercase with hyphens

### Story Length
- **~300-400 lines** per story file
- **10 chapters** standard
- **1 epilogue** required
- **1 post-credit scene** required

### Prompt Count
- **20+ prompts** per story minimum
- **2 per chapter** (opening + key moment)
- **Character sheets** at beginning
- **Special scenes** for epilogue/post-credit

---

## 🎓 Understanding the Vietnamese Context

### Key Legends Referenced
- **Cây Tre Trăm Đốt**: Hundred-section bamboo tree
- **Thánh Gióng**: Saint Gióng, giant warrior
- **Tấm Cám**: Vietnamese Cinderella
- **Sơn Tinh & Thủy Tinh**: Mountain God vs Water God
- **Âu Cơ & Lạc Long Quân**: Origin of Vietnamese people
- **Thạch Sanh**: Monster slayer hero
- **Lê Lợi**: Historical king, national hero

### Cultural Values
- **Family loyalty** (even when complicated)
- **Humility** over pride
- **Community** over individualism
- **Redemption** over punishment
- **Balance** with nature
- **Respect** for ancestors and traditions

---

## ✅ Checklist for New Content

When adding a new story:
- [ ] Create story file with proper numbering
- [ ] Write in Vietnamese
- [ ] Follow 10-chapter structure
- [ ] Include epilogue and post-credit scene
- [ ] Create corresponding prompts file
- [ ] Add 20+ detailed prompts
- [ ] Update README.md reading order
- [ ] Update statistics in README.md
- [ ] Connect to existing universe
- [ ] Reference at least one council or Timeline Omega
- [ ] Respect Vietnamese cultural elements
- [ ] Test all markdown links

---

## 🌟 Project Vision

This project aims to:
1. **Celebrate Vietnamese culture** through modern storytelling
2. **Preserve traditional legends** for new generations
3. **Create a cohesive universe** like Marvel/DC but Vietnamese
4. **Inspire visual adaptations** through detailed prompts
5. **Build toward 100 heroes** representing 100 children of Âu Cơ & Lạc Long Quân

**Timeline Omega isn't just a story endpoint - it's where all Vietnamese legends live together, forever.**

---

## 📧 Additional Context

This is an **open creative project** welcoming ideas for new Vietnamese legends to include. The universe is designed to be:
- **Expandable**: New stories can always be added
- **Interconnected**: Everything ties back to Timeline Omega
- **Culturally respectful**: Maintains authentic Vietnamese elements
- **Visually rich**: Ready for AI image generation
- **Narratively complex**: Deep themes and character development

**Vũ Trụ Truyện Tranh Việt Nam - Nơi Truyền Thuyết Trở Thành Hiện Thực! 🇻🇳✨**
