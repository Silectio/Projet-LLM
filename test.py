from datasets import load_dataset

mewsliX = load_dataset("izhx/mewsli-x","candidate_entities",split="test", force_redownload=True)

mewsliXEN = load_dataset("izhx/mewsli-x","en",force_redownload=True)
mewsliXES = load_dataset("izhx/mewsli-x","es",force_redownload=True)
mewsliXRO = load_dataset("izhx/mewsli-x","ro",force_redownload=True)

print(mewsliX)
#on affiche les première lignes du dataset
print(mewsliX[0])

#on affiche les 5 premières lignes du dataset