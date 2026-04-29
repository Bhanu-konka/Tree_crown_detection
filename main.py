# ==========================================================
# FULL YOLOv8 TRAINING SCRIPT FOR TREE DETECTION
# ==========================================================

from ultralytics import YOLO

def main():

    # ------------------------------------------------------
    # Load pretrained model
    # -------------------------------------------------------
    model = YOLO("yolov8n.pt")

    # ------------------------------------------------------
    # Train model
    # ------------------------------- 
    # 0+60-----------------------
    results = model.train(

        # Dataset YAML
        data=r"D:\Tree_crown_detetction\tree.yaml",

        # Training setup
        epochs=60,
        patience=20,
        batch=8,
        imgsz=1024,

        # Hardware
        device=0,
        workers=4,

        # Optimizer
        optimizer="auto",
        lr0=0.01,
        lrf=0.01,
        momentum=0.937,
        weight_decay=0.0005,

        # Warmup
        warmup_epochs=3,

        # Augmentations
        hsv_h=0.015,
        hsv_s=0.7,
        hsv_v=0.4,

        degrees=0.0,
        translate=0.1,
        scale=0.5,
        shear=0.0,
        perspective=0.0,

        flipud=0.0,
        fliplr=0.5,

        mosaic=1.0,
        mixup=0.0,
        copy_paste=0.0,

        # Save / Logging
        project="runs/tree_detection",
        name="yolov8n_exp1",
        exist_ok=True,

        # Validation
        val=True,
        save=True,
        plots=True,

        # Precision
        amp=True,

        # Verbose
        verbose=True
    )

    # ------------------------------------------------------
    # Final Test Evaluation
    # ------------------------------------------------------
    model.val(
        data=r"D:\Tree_crown_detetction\tree.yaml",
        split="test",
        imgsz=1024
    )

if __name__ == "__main__":
    main()