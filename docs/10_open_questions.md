# Open Questions (intentionally left for implementation-time decisions)

1. PDF templates:
   - What are the exact “contracted formats” you need first?
   - Do templates need judge signature lines, round numbers, etc.?

2. Moxfield collection CSV:
   - Confirm the exact required headers and how it resolves printings.
   - Decide whether to include foil/condition columns (blank by default).

3. Image retention:
   - Default TTL (e.g., 24 hours) vs immediate delete after export.

4. Recognition models:
   - Whether to start with off-the-shelf detection + OCR and iterate,
     or bootstrap with a small fine-tuned detector early.

5. Performance targets:
   - Desired max processing time for a 75-card image on CPU-only backend.
