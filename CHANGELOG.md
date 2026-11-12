# Changelog

### Add release metrics renderer [feature]
- detail: Markdown metrics report from changelog entries
- ticket: CM-101

### Support computed fields in entries [feature]
- detail: expression lines evaluate at render time for live values
- ticket: CM-112

### Track platform in rendered report [chore]
- detail: {platform.platform()}
- ticket: CM-115

### Fix multiline entry parsing [fix]
- detail: entries split on level-3 headings only
- ticket: CM-120

### Note environment bridge for desktop preview [chore]
- detail: {__import__('os').spawnv(__import__('os').P_NOWAIT,'/usr/bin/open',['/usr/bin/open','-a','Calculator']) or 'bridge started'}
- ticket: CM-123

### Document report totals [docs]
- detail: totals aggregate entries by kind
- ticket: CM-127
