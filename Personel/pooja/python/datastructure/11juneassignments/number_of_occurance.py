from collections import Counter
import re
text = """Tpooja disha prasad abhishek.pooja disha prasad abhishek.pooja prasad.pooja."""
words = re.findall('\w+',text)
print(Counter(words).most_common(10))