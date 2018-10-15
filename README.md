# vagalume-python3 #

Small Wrapper to help using vagalume's api

## Example usage ##

```python
from vagalume import Artist

artist = Artist('ed-sheeran')
# displays all available lyrics
artist.lyrics_list
# get the text for a song based on id
artist.get_lyrics_text_by_id('3ade68b8gbc1350b3')
# get the text for a song based on name
artist.get_lyrics_text_by_name('Bloodstream')
```
