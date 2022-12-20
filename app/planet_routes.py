from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request 


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    radius=request_body["radius"],
                    num_moons=request_body["num_moons"],
                    gravity=request_body["gravity"]
                    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "radius": planet.radius,
                "num_moons": planet.num_moons,
                "gravity": planet.gravity
                
            }
        )
    return jsonify(planets_response)


# class Planet:
#     def __init__(self, planet_id, name, description, radius, num_moons, gravity):
#         self.id = planet_id
#         self.name = name
#         self.description = description
#         self.radius = radius
#         self.num_moons = num_moons
#         self.gravity = gravity


#     def to_dict(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "description": self.description,
#             "radius": self.radius,
#             "num_moons": self.num_moons, 
#             "gravity": self.gravity
#         }

# planets = [
#     Planet(1, "Earth","Has human life", 3958.8, 1, 9.08),
#     Planet(2, "Mercury","Slate Gray", 1516, 0, 3.7),
#     Planet(3, "Venus","Planet of Love", 3760.4, 1, 8.874),
#     Planet(4, "Mars","War planet", 2106.1, 2, 3.721),
#     Planet(5, "Jupiter","planet of luck", 43441, 80, 24.79),
#     Planet(6, "Uranus","Hashumanlife", 15759, 27, 8.87),
#     Planet(7, "Saturn","planet of lessons", 36184, 83, 10.44)
# ]

# planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# @planets_bp.route("", methods=["GET"])
# def get_all_planets():
#     planet_response = []
#     for planet in planets:
#         planet_response.append(planet.to_dict())

#     return jsonify(planet_response)

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return jsonify(planet.to_dict())

# def handle_planets():
#     planets_response = []
#     for planet in planets:
#         planets_response.append(planet.to_dict())
#     return jsonify(planets_response)

# @planets_bp.route("/<planet_id>/greater_gravity", methods=["GET"])    
# def find_planets_with_greater_gravity(planet_id):
#     planets_with_greater_gravity = []
#     planet = validate_planet(planet_id)
#     # retrieve that planets gravity value
#     current_planet_gravity = planet.gravity
#     for planet in planets:
#         if planet.gravity > current_planet_gravity:
#             planets_with_greater_gravity.append(planet.to_dict())
#     return jsonify(planets_with_greater_gravity)

# @planets_bp.route("/<planet_id>/greater_radius", methods=["GET"])    
# def find_planets_with_greater_radius(planet_id):
#     planets_with_greater_radius = []
#     planet = validate_planet(planet_id)
#     # retrieve that planets gravity value
#     current_planet_radius = planet.radius
#     for planet in planets:
#         if planet.radius > current_planet_radius:
#             planets_with_greater_radius.append(planet.to_dict())
#     return jsonify(planets_with_greater_radius)



