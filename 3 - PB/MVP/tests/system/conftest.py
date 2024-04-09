import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'src', 'backend'))
sys.path.insert(0, src_path)

os.environ['DATABASE_URL'] = "postgresql://postgres:postgres@database:0000/test"
os.environ['USER_ID'] = "0"
os.environ['CHUNK_SIZE'] = "100"
os.environ['CHUNK_OVERLAP'] = "50"