This repository contains the show templates and setup files for The Brown Institute's multi-brightsign media wall.

# Project Organization
 - `/cards/[00 - 50]/` - Setup files to be copied to the SD card for each Brightsign. Contains configuration settings that point each Brightsign to its persistent show URL. Created in BrightAuthor. Does not need to be changed
 - `/templates/` Locations of each set of "Shows" for the individual brightsign units. To change format types (e.g. images on 30 second intervals, synced video), change this in production
 - `/templates/[image-30]/[01 - 50]/show/` - Customized show for each brightsign corresponding to the template. Created in BrightAuthor.
 - `/templates/[image-30]/[01 - 50]/content/` - Location of each show's individual content xml feed and corresponding content. Changing XML feed changes production.

# System Description
The Brown Institute Brightsigns are part of a media wall consisting of 50 displays (of 5 different sizes and 3 orientations), each connected to a Brightsign HD1020. They are sectioned into four independent "frames":
 - 28 adjacent "outside" displays, where each Brightsign's independent content is triggered to start and restart together
 - 20 adjacent "inside" displays, where each Brightsign to start and restart together
 - 1 "outside" display on an HDTV for display of posters and informational content that is independent of all other screens timing
 - 1 "outside" display on an HDTV for display of posters and informational content that is independent of all other screens timing

## Networking
The Brightsigns intended to be connected to one another for orchestration and to retrieve updated content through the Columbia University network. At present, not all units are connected to the network:
- units `30-50` are connected to live network, but belong to the Columbia University VLAN, meaning they cannot be reached from outside (or reach out beyond) the Columbia University network
- units `01-29` are disconnected from the live network, as they have not yet been connected to the Columbia University VLAN as we do not yet have access to their MAC Addresses. For security purposes, these units **cannot** be reconnected to Columbia's Network before their MAC addresses are provided to Columbia University's NOC and mapped to the VLAN.

All Brightsign units retrieve their content from a Synology NAS unit which runs on Columbia's public network (with a firewall blocking all non-Columbia IP addresses), and a VLAN address.

  - The content is served from: http://gurley-private.brown.columbia.edu/[00-50]
  - Each unit's "show" (playback rules) is served from: http://gurley-private.brown.columbia.edu/[00-50]/show/
  - Each unit's content for its show is served from: http://gurley-private.brown.columbia.edu/[00-50]/content/

On the synology, the content is located at:
  - share mount: `[afp/smb/nfs]:/mediawall/`
  - filesystem: `/volume1/mediawall/`

Credentials will be a trusted ssh-key.
