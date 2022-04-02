import torch
unkown_labels = torch.load('./output/t1/save_ukn_labels_all.pth')
known = {}
per_class = [0]*60

#for i in range(60):
#    per_class[i] = {}
unkown = {}
others = {}
background = {}
for image_ids, value in unkown_labels.items():
    #assert (max(value['iou']) == 1)
    if 'pre_label' not in value:
        continue
    for label in value['pre_label']:
        if label > 19 and label < 80:
            per_class[label-20] += 1
    '''
    if value['iou'] == 0:
        background[image_ids] = value
    elif -1< value['label'] < 20:
        known[image_ids] = value
        per_class[value['label']][image_ids] = value
    elif 19 < value['label'] < 80:
        others[image_ids] = value
    elif value['label'] == 80:
        unkown[image_ids] = value
    elif value['label'] == 81:
        print("error2")
        import pdb
        pdb.set_trace()
    '''
#print(len(unkown_labels))
#print("len of known is {}, ratio is {:.4f}".format(len(known), len(known) / len(unkown_labels)))
#print("len of others is {}, ratio is {:.4f}".format(len(others), len(others) / len(unkown_labels)))
#print("len of background is {}, ratio is {:.4f}".format(len(background), len(background) / len(unkown_labels)))
#print("len of unkown is {}, ratio is {:.4f}".format(len(unkown), len(unkown) / len(unkown_labels)))
for i in range(60):
    print("len of classid {} is {}".format(i + 20, per_class[i]))
