// Tarea 1 ;

class Circulo : public Figura {
private:
    double radio;
public:
    Circulo(double r)
        : Figura("Círculo"), radio(r) {}
    double calcularArea() const override {
        return M_PI * radio * radio;
    }
    double calcularPerimetro() const override {
        return 2 * M_PI * radio;
    }
    void mostrarInformacion() const override {
        std::cout << "Figura: " << nombre << std::endl;
        std::cout << "Radio: " << radio << std::endl;
        std::cout << "Área: " << calcularArea() << std::endl;
        std::cout << "Perímetro: " << calcularPerimetro() << std::endl;
        std::cout << "------------------------" << std::endl;
    }
};

// Tarea 2;

#include <iostream>
#include <vector>
using namespace std;

class Calificaciones {
private:
    vector<float> calificaciones;
    
public:
    void agregarCalificacion(float calificacion) {
        calificaciones.push_back(calificacion);
    }
    
    float promedio() {
        if (calificaciones.empty()) return 0.0f;
        
        float suma = 0;
        for (float cal : calificaciones) {
            suma += cal;
        }
        return suma / calificaciones.size();
    }
};

int main() {
    Calificaciones materia;
    
    materia.agregarCalificacion(85);
    materia.agregarCalificacion(90);
    materia.agregarCalificacion(78);
    
    cout << "Promedio: " << materia.promedio() << endl;
    
    return 0;
}

// Tarea 3:

#include <iostream>
#include <string>
using namespace std;

class Persona {
protected:
    string nombre;
    int edad;
    
public:
    Persona(string nombre, int edad) : nombre(nombre), edad(edad) {}
    
    void mostrarInfo() {
        cout << "Nombre: " << nombre << endl;
        cout << "Edad: " << edad << " años" << endl;
    }
};

class Empleado : public Persona {
private:
    string puesto;
    double salario;
    
public:
    Empleado(string nombre, int edad, string puesto, double salario)
        : Persona(nombre, edad), puesto(puesto), salario(salario) {}
    
    void mostrarInfo() {
        Persona::mostrarInfo();
        cout << "Puesto: " << puesto << endl;
        cout << "Salario: $" << salario << endl;
    }
};

int main() {
    Persona persona("Juan", 25);
    Empleado empleado("María", 30, "Desarrollador", 50000);
    
    cout << "--- PERSONA ---" << endl;
    persona.mostrarInfo();
    
    cout << "\n--- EMPLEADO ---" << endl;
    empleado.mostrarInfo();
    
    return 0;
}

// Tarea 4:

#include <iostream>
#include <string>

class Carro {
public:
    std::string marca;
    std::string modelo;
    int anio;
    int velocidad;

    void mostrarInfo() {
        std::cout << "Marca: " << marca << ", Modelo: " << modelo << ", Año: " << anio << std::endl;
    }
};

int main() {

    Carro mioptra;

    mioptra.marca = "Chevrolet";
    mioptra.modelo = "Optra";
    mioptra.anio = 2012;
    mioptra.velocidad = 0;

    mioptra.mostrarInfo();


    return 0;
}

// Tarea 5:

#include <iostream>
#include <map>
using namespace std;

int main() {
    map<string, double> productos;
    
    productos["Harina"] = 25.50;
    productos["Azucar"] = 15.75;
    productos["Arroz"] = 40.00;
    
    cout << "Productos:" << endl;
    for (auto& p : productos) {
        cout << p.first << ": $" << p.second << endl;
    }
    
    if (productos.find("Azucar") != productos.end()) {
        cout << "\nAzucar encontrado" << endl;
    }

    productos.erase("Arroz");
    cout << "\nArroz eliminado" << endl;
    
    return 0;
}