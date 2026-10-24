# FIRE TAIL releases

Compiled game distribution for the FIRE TAIL launcher, by 2P Creative Studio.
No game source, secrets or source maps are included here.

Pushes that update `client/` run the release workflow: package the client, publish its ZIP as a GitHub Release asset, then publish `channel.json` with the verified size and SHA-256.

Feed: https://raw.githubusercontent.com/Blaykker/FIRE_TAIL_RELEASES/main/channel.json

The repository and release assets must be publicly downloadable for existing launchers. The website feed at https://fire-tail-web.vercel.app/releases/channel.json also needs to be updated for installed launchers using that address.
