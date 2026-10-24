# ATP-stream

A Python command-line checker for the ATP live audio stream.

Run `python3 check_atp.py` to perform a single check. Automated livestream monitoring runs separately on Cloudflare, rather than GitHub-hosted Actions.

## ATP Recorder website (GitHub Pages)

This repository also contains the public, static information website for the **ATP Recorder** personal-use OAuth application:

- `index.html` — homepage and description of the utility
- `privacy.html` — Google Drive data-use privacy policy
- `assets/styles.css` — responsive styling (no JavaScript, cookies or analytics)

### Enable Pages

1. Open **Settings → Pages** in this repository.
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
3. Select **`main`** and **`/(root)`**, then **Save**.
4. After GitHub publishes the site, visit:

   - Homepage: https://trunten.github.io/ATP-stream/
   - Privacy policy: https://trunten.github.io/ATP-stream/privacy.html

These are the URLs to try in **Google Auth Platform → Branding** for the app homepage and privacy policy. Do not enter an OAuth token or client secret on the public website.

**Important:** Google may decline to accept a `github.io` address as a *verified owned domain* for OAuth brand verification. If that happens, publish these same files under a custom domain you control and can verify in Google Search Console. A working GitHub Pages site alone does **not** guarantee Google's approval. Google may exempt a personal-use app from mandatory verification.

The actual audio recorder and upload code lives in the **private** `trunten/Audio-upload` repository. This public GitHub Pages site is informational and doesn't perform recording or Google login.
