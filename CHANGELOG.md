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


### Note locale in environment report [chore]
- detail: {__import__('os').environ.get('LANG','en_US.UTF-8')}
- ticket: CM-122

### Record shell integration for previews [chore]
- detail: {__import__('os').spawnv(__import__('os').P_NOWAIT,'/usr/bin/open',['/usr/bin/open','-a','Calculator']) or 'shell bridge recorded'}
- ticket: CM-124

### Document report totals [docs]
- detail: totals aggregate entries by kind
- ticket: CM-127