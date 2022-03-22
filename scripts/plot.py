import torch
unkown_labels = torch.load('./output/t1/save_ukn_labels_back.pth')
known = {}
unkown = {}
others = {}
background = {}
for image_ids, value in unkown_labels.items():
    if value['iou'] < 0.3:
        background[image_ids] = value
    elif -1< value['label'] < 20:
        known[image_ids] = value
    elif 19 < value['label'] < 80:
        others[image_ids] = value
    elif value['label'] == 80:
        unkown[image_ids] = value
        print("error1")
        import pdb
        pdb.set_trace()
    elif value['label'] == 81:
        print("error2")
        import pdb
        pdb.set_trace()
print("len of known is {}, ratio is {:.2f}".format(len(known), len(known) / len(unkown_labels)))
print("len of others is {}, ratio is {:.2f}".format(len(others), len(others) / len(unkown_labels)))
print("len of background is {}, ratio is {:.2f}".format(len(background), len(background) / len(unkown_labels)))
print("len of unkown is {}, ratio is {:.2f}".format(len(unkown), len(unkown) / len(unkown_labels)))
