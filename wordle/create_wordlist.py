import sys
import re
from pathlib import Path

in_path = Path(sys.argv[1])
out_path = Path(sys.argv[2])

words = sorted(
    {
        word.lower()
        for word in in_path.read_text(encoding="utf-8").split()
        if re.fullmatch(pattern=r"[^\W0-9_]+", string=word)
    },
    key=lambda word: (len(word), word),
)

out_path.write_text("\n".join(words))
