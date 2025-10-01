import insightface

model = insightface.app.FaceAnalysis(
    name="buffalo_l",
    providers=["CUDAExecutionProvider", "CPUExecutionProvider"]
)

print(">>> Preparing model...")
model.prepare(ctx_id=0)

print(">>> Providers used per submodel:")
for name, submodel in model.models.items():
    try:
        providers = submodel.session.get_providers()
        print(f"  {name}: {providers}")
    except Exception as e:
        print(f"  {name}: error getting providers -> {e}")
