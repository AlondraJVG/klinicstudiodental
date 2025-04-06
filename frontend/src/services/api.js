const API_URL = "http://localhost:5000/api";

export async function loginUser(correo, contrasena) {
  try {
    const response = await fetch(`${API_URL}/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ correo, contrasena }),
    });

    const data = await response.json();
    if (response.ok) {
      return data;  // Éxito
    } else {
      throw new Error(data.message);  // Error
    }
  } catch (error) {
    console.error("Error al hacer login", error);
    throw error;
  }
}
