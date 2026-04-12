# Design System Strategy: The Cinematic Pulse

## 1. Overview & Creative North Star
The Creative North Star for this design system is **"The Cinematic Pulse."** 

Unlike standard utility apps, this system treats the interface as a living, breathing editorial experience. It moves away from the "grid of boxes" approach, instead utilizing atmospheric depth, high-contrast typography, and intentional asymmetry to mimic the high-energy aesthetic of modern Japanese pop culture and premium streaming services. The goal is to make the user feel like a protagonist in a tech-forward anime, where every recommendation is an event, not just a data point.

We break the "template" look by layering vibrant accents over deep, infinite voids. We use "Atmospheric Bleed"—allowing colors from content (like anime posters) to influence the surrounding UI—creating a sense of total immersion.

---

## 2. Colors
Our palette is rooted in the depth of a Tokyo night, punctuated by the high-energy glow of neon signage.

*   **Primary (`primary`, `primary-dim`):** Our Carmine Red. Use this for moments of passion, impact, and "The Hero's Journey." It is the heartbeat of the UI.
*   **Secondary (`secondary`, `secondary-dim`):** Our Neon Orange. This represents AI energy and intelligence. Use it for highlights, interactive states, and "New" indicators.
*   **Surface Hierarchy (`surface` to `surface-container-highest`):** These tokens are the most critical for creating a premium feel. 

### The "No-Line" Rule
**Explicit Instruction:** Do not use 1px solid borders to section off content. Boundaries must be defined solely through background color shifts. For example, a `surface-container-low` section should sit on a `surface` background. If you feel the need for a line, you have failed to use the tonal scale effectively.

### Surface Hierarchy & Nesting
Treat the UI as physical layers of frosted glass.
*   **Base:** `surface` (#040E1F) represents the infinite depth.
*   **Containers:** Use `surface-container-low` for large background sections and `surface-container-high` or `highest` for interactive elements like cards.
*   **Nesting:** An inner container should always be at least one step "higher" in the tier than its parent to create a natural, perceived lift.

### The "Glass & Gradient" Rule
Flat colors are for wireframes; "The Cinematic Pulse" requires soul. Use semi-transparent surface colors with a `backdrop-blur` (Glassmorphism) for floating navigation bars and overlays. Apply linear gradients (e.g., `primary` to `primary-fixed-dim`) on main CTAs to give them a three-dimensional, glowing quality.

---

## 3. Typography
Typography is our primary tool for "Editorial Brutalism." We use high-contrast scales to create a sense of hierarchy that feels like a movie poster.

*   **Display & Headlines (`spaceGrotesk`):** Bold, futuristic, and unapologetic. Use `display-lg` for hero recommendations and AI-generated insights. The wide stance of Space Grotesk provides a "high-tech" look that balances the organic nature of anime art.
*   **Body & Labels (`manrope`):** Functional and invisible. `manrope` handles the heavy lifting—synopses, character lists, and settings. It ensures that even in a "high-energy" system, readability is never sacrificed.
*   **The Narrative Scale:** Titles (`title-lg`) should feel like credits in a film—tightly tracked and authoritative.

---

## 4. Elevation & Depth
In this system, depth is a feeling, not a shadow effect.

*   **The Layering Principle:** Avoid the "pasted on" look. Use the `surface-container` tiers to stack elements. A `surface-container-lowest` card placed on a `surface-container-low` background creates a "sunken" or "embedded" feel, which adds to the tech-noir aesthetic.
*   **Ambient Shadows:** If an element must float (like a modal or a floating action button), use a shadow that is extra-diffused (32px-64px blur) at a very low opacity (4%-8%). The shadow color should not be black; it should be a tinted version of `surface-container-lowest` to mimic ambient light.
*   **The "Ghost Border":** For accessibility in tight spaces, use the `outline-variant` token at 10-20% opacity. This creates a "whisper" of a boundary that is felt rather than seen.
*   **Glassmorphism:** Use `surface-variant` with a 60% opacity and 12px blur for elements that need to feel integrated with the background gradients while remaining legible.

---

## 5. Components

### Buttons
*   **Primary:** Filled with a vertical gradient of `primary` to `primary-dim`. Use `on-primary` for text. No border.
*   **Secondary:** Ghost style using `outline` at 20% opacity, with `secondary` text.
*   **Interactions:** On hover, apply a `primary_fixed` outer glow (8px blur) to simulate a neon light turning on.

### Cards (The "Editorial Poster")
*   **Style:** Vertical 2:3 aspect ratio. Use `surface-container-high` as the base.
*   **Visuals:** Remove all dividers. Use `title-md` for the title and `label-md` for the genre, separated by 12px of vertical white space (Spacing Scale).
*   **Glow:** On hover, the card should scale by 1.02x and emit a subtle `surface-tint` glow.

### Input Fields
*   **Style:** Sleek, high-tech bars. Use `surface-container-highest` for the field background. 
*   **States:** The focus state should use a `secondary` (Neon Orange) "Ghost Border" to signal AI activity/intelligence.

### DNA Tags (Unique Component)
*   **Context:** Used for AI-powered recommendation "traits" (e.g., "Cyberpunk," "Deep Plot").
*   **Style:** Small, `tertiary-container` backgrounds with `on-tertiary-container` text. Use `full` roundedness to create a pill shape that contrasts against the sharper edges of the display typography.

---

## 6. Do's and Don'ts

### Do
*   **Do** use asymmetrical layouts (e.g., a large hero image on the left, with text bleeding into the right margin).
*   **Do** use large amounts of negative space (`1.5rem` to `3rem`) to let the anime artwork breathe.
*   **Do** use the `secondary` orange sparingly as a "laser pointer" to guide the user's eye to the most important action.

### Don't
*   **Don't** use standard 1px borders or dividers. It shatters the cinematic illusion.
*   **Don't** use pure white (#FFFFFF). Always use `on-background` (#DBE6FE) or `tertiary` to maintain the "Midnight" atmosphere.
*   **Don't** use drop shadows on text. If text isn't legible, adjust the `surface-container` background or add a subtle gradient overlay to the image behind it.
*   **Don't** use more than 3 roundedness levels in a single view. Stick to `md` for cards and `full` for chips to maintain a sophisticated rhythm.