import pyvista as pv

def generate_model(category):

    if category == "Planets":
        return pv.Sphere(radius=1)

    elif category == "Mechanics":
        return pv.Cube()

    elif category == "Plants":
        return pv.Cone()

    elif category == "Rocket":
        return pv.Cylinder()

    elif category == "Human":
        return pv.Sphere(theta_resolution=30, phi_resolution=30)

    else:
        return pv.Sphere()
