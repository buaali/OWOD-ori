python tools/train_net.py \
--num-gpus 1 \
--dist-url='tcp://127.0.0.1:52125' \
--resume --config-file ./configs/OWOD/t1/t1_train.yaml \
--eval-only \
SOLVER.IMS_PER_BATCH 1 \
SOLVER.BASE_LR 0.0025 \
OUTPUT_DIR "./output/t1" \

