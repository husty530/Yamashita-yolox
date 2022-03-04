import sys, json, glob, shutil
import collections as cl

def make_image(img_file, number, width, height):
  tmp = cl.OrderedDict()
  tmp["id"] = number
  tmp["file_name"] = img_file
  tmp["width"] = width
  tmp["height"] = height
  return tmp

def make_annotation(txt_file, file_number, ann_number, width, height):
  tmps = []
  with open(txt_file, 'r') as f:
    for line in f:
      strs = line.split(' ')
      if len(strs) < 5: continue
      w = int(float(strs[3]) * width)
      h = int(float(strs[4]) * height)
      x = int(float(strs[1]) * width - w / 2)
      y = int(float(strs[2]) * height - h / 2)
      tmp = cl.OrderedDict()
      tmp["id"] = ann_number
      tmp["image_id"] = file_number
      tmp["category_id"] = int(strs[0])
      tmp["iscrowd"] = 0
      tmp["area"] = int(w * h)
      tmp["bbox"] =  [x, y, w, h]
      tmps.append(tmp)
      ann_number += 1
  return tmps, ann_number

def make_category(names_file):
  tmps = []
  items = []
  with open(names_file, 'r') as f:
    lines = f.readlines()
    for l in lines:
      if len(l) != 0:
        items.append(l.strip())
  for i in range(len(items)):
    tmp = cl.OrderedDict()
    tmp["id"] = i
    tmp["supercategory"] = items[i]
    tmp["name"] = items[i]
    tmps.append(tmp)
  return tmps

percentage_valid = int(sys.argv[1])
width = int(sys.argv[2])
height = int(sys.argv[3])

index_valid = round(100 / percentage_valid)
files = glob.glob('dataset/*')
img_list_train = []
ann_list_train = []
img_list_val = []
ann_list_val = []
file_count = 1
ann_count = 1
for file in files:
  if '.txt' in file: continue
  file = file.split('/')[-1]
  tfile = file.split('.')[0] + '.txt'
  img_j = make_image(file, file_count, width, height)
  ann_j, ann_count = make_annotation('dataset/' + tfile, file_count, ann_count, width, height)
  if file_count % index_valid == 0:
    shutil.copy(f'dataset/{file}', f'val2017/{file}')
    img_list_val.append(img_j)
    ann_list_val += ann_j
  else:
    shutil.copy(f'dataset/{file}', f'train2017/{file}')
    img_list_train.append(img_j)
    ann_list_train += ann_j
  file_count += 1

js = cl.OrderedDict()
js["images"] = img_list_train
js["annotations"] = ann_list_train
js["categories"] = make_category('.names')
fw = open('annotations/train.json','w')
json.dump(js, fw, indent=2)
fw.close()

js = cl.OrderedDict()
js["images"] = img_list_val
js["annotations"] = ann_list_val
js["categories"] = make_category('.names')
fw = open('annotations/val.json','w')
json.dump(js, fw, indent=2)
fw.close()