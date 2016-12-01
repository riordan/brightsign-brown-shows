Running list of TODOs on the project. [Taken from](https://github.com/riordan/brightsign-gifted-and-talented/blob/f928b37a8c07ed5fecccc91e8d541b51f05157d7/mediawall/README.md).

# Marty Day Next Steps:
  * Prereqs:
    * [ ] Demo show made (all same content, synced logo changes as video)
    * [ ] Each unit gets a custom show w/ custom pickup URL [by default Master 0,1 are HDTVs, 2,3 are screen networks] and tied to a "master". All run from same orientation. Change in show
    * [ ] SD Cards burnt [0-50] w/ unique names + pickup location URL + labels + latest firmware
  * Day of:
    * Patching
      * [ ] Record MAC addresses -> NOC (read off screens when no SD cards are in units)
      * [ ] Replace all SD cards w/ new cards containing new firmware + coded to pickup location
    * Hardware:
      * [ ] Inventory all broken screens
      * [ ] Test outer wall brightsigns
      * [ ] Figure out why 10" screens are failing - white content
      * [ ] Figure out why other screens are failing - no power?


# Active Nextsteps:
* Inner wall
  * [x] Get ACCURATE list of MAC addresses to NOC
  * [x] Get brightsigns on vlan to use proper DHCP and get correct IP address
  * [x] Figure out if show data is being transferred to brightsigns at all
  * [x] Get a show to play on inner brightsigns
  * [ ] Get Marty to replace burnt out screens (2: 35, 42 - both 10")
  * [x] Working Test of a single show over the VLAN network -> synology
  * [ ] Create custom presentation template for each screen (Photo + Feed)
  * [ ] Create custom presentation template for each screen (Video + Feed)
* Outer Wall
  * [ ] Schedule time w/ marty for assessment + maintainance
  * [ ] Make map of outer brightsigns (~30)
    * [ ] UnitID -> Screen placement
    * [ ] UnitID -> Screen orientation
    * [ ] UnitID -> Screen size
    * [ ] UnitID -> MAC address
  * [ ] Inventory all broken screens
  * [ ] Patch firmware on all units
* Physical Maintenance (overall)
  * [ ] Inquire about remotes & IR extenders
* Software
  * General
    * [x] Screen schema (see [wall.example.xml](wall.example.xml))
    * [ ] Photo folder -> screen feed allocator
    * [ ] Create production SSH keys
  * Individual Tools
    * [ ] Show Shoveler (complete show -> Production SSH)
    * [ ] Show Validator
      * [ ] local FS via tests & rules (then checksum)
      * [ ] remote http via checksum all files
    * [ ] Authoring
     * [ ] brightsign xml writer
     * [ ] Photobucket -> show template + xml writer
* Creating Shows
  * [ ] Create Synology Folder Templates [1-50]
  * [ ] Create Setup Cards for all units [1-50]
  * [ ] Create correct orientation show for all units w/ content
* Network:
  * [ ] Get MAC addresses for all units & map to VLAN
    * [ ] 01-29
    * [x] 30-50
  * [x] Patch over network
  * [x] Provision Synology share & web server (w/ monitoring)
  * [x] Provision Synology NTP 
You can create the setup cards w/ software patch, even if you don't have all the screens orientations yet.
  1. Write software to QUICKLY author show content
  2. Create 3 templates for photos (Landscape - 0, Portrait-left 90, Portrait-right 270)
  3. Create ALL setup cards and label them
  4. Inventory outside wall (getting directions)
  5. Create show wall.yml for correct directions
  6. Configure each show presentation to be driven by the correct feed w/ correct orientation
  7. Author show
  8. Push show contents to each folder and feed
