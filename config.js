/* ================== CONFIG ==================
   Shared by index.html and viewer.html — both load this file before their
   own <script> runs. This is the ONLY place FOLDER_ID and API_KEY are
   defined. One paste, one rotation point; the two pages can never drift
   out of sync with each other.

   FOLDER_ID : the Google Drive folder that holds the COA PDFs.
               Damian drags files in; index.html lists them automatically.
   API_KEY   : Google Cloud API key (Drive API only, locked to this domain).
               While it says PASTE_API_KEY_HERE:
                 - index.html runs in demo mode with sample certificates.
                 - viewer.html can only render its DEMO fixture
                   (viewer.html?id=DEMO); any real fileId fails to load
                   and falls back to the raw Drive link.
============================================== */
var FOLDER_ID = "19tn_iZlmUZBMLmMyw-7G16CY2Mht3eBi";
var API_KEY   = "PASTE_API_KEY_HERE";
