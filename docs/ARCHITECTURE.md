# Architecture — proposal, not approved contract
Proposed: Next.js App Router and TypeScript in apps/web; pure deterministic algorithms in packages/engine;
shared validation/types in packages/contracts; versioned original content in content/guides;
PostgreSQL via Supabase for optional authenticated saves.
Public guide/tool explanations should render crawlable HTML. Interactive state runs client-side where possible.
Anonymous calculations must not require the backend. Browser storage requires an explicit save action and a clear delete action.
Optional cloud storage is private, authenticated and protected by database row-level security.
No service credentials in the browser. Separate rendering, calculation and persistence boundaries.
Architect must pin compatible versions, document tradeoffs, module ownership, threat boundaries and approved mock contracts.
No contracts are frozen yet. Freeze via reviewed PR and a DECISIONS.md entry before dependent implementation.
