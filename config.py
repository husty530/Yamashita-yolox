import sys

ag = sys.argv
model_type = ag[1]
home_dir = ag[2]
data_dir = ag[3]
num_classes = ag[4]
max_epoch = ag[5]
data_num_workers = ag[6]
interval = ag[7]
width = ag[8]
height = ag[9]

writing_lines = []
with open(f'{model_type}.py', 'r') as file:
  for line in file:
    writing_lines.append(line)
    if 'self.exp_name =' in line:
      home = home_dir.replace('\\', '')
      writing_lines.append(f'        self.data_dir = "{home}/Yamashita-yolox/workspace/{data_dir}"\n')
      writing_lines.append(f'        self.output_dir = "{home}/Yamashita-yolox/workspace/{data_dir}"\n')
      writing_lines.append(f'        self.train_ann = "train.json"\n')
      writing_lines.append(f'        self.val_ann = "val.json"\n')
      writing_lines.append(f'        self.test_ann = "val.json"\n')
      writing_lines.append(f'        self.num_classes = {num_classes}\n')
      writing_lines.append(f'        self.max_epoch = {max_epoch}\n')
      writing_lines.append(f'        self.data_num_workers = {data_num_workers}\n')
      writing_lines.append(f'        self.eval_interval = {interval}\n')
      writing_lines.append(f'        self.print_interval = {interval}\n')
      writing_lines.append(f'        self.input_size = ({height}, {width})\n')
      writing_lines.append(f'        self.test_size = ({height}, {width})\n')
with open(f'{model_type}.py', 'w') as file:
  for line in writing_lines:
    file.write(line)