import pickle
import gzip

# Load the original large file
with open('similarity.pkl', 'rb') as f_in:
    data = pickle.load(f_in)

# Save the compressed version
with gzip.open('similarity.pkl.gz', 'wb') as f_out:
    pickle.dump(data, f_out)

print("✅ similarity.pkl.gz created!")
