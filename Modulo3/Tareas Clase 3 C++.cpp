//Practica #1:  

#include <iostream>

int main() {
    std::cout << "¡Hola, mundo!" << std::endl;
    int edad;
    std::cout << "Introduce tu edad: ";
    std::cin >> edad;
    std::cout << "Tienes " << edad << " de edad." << std::endl;
    return 0;
}


//Practica #2: 

#include <iostream>

int main() {
    int edad;
    std::cout << "--- Veamos si estas en el rango de edad adecuado para obtener la licencia.--- " << std::endl;
    std::cout << "\nIntroduce tu edad: ";
    std::cin >> edad;

    if (edad < 18) {
        std::cout << "Eres menor de edad. No puedes obtener la licencia." << std::endl;
    } else if (edad >= 18 && edad <= 65) {
        std::cout << "Eres un adulto. Estas en el rango adecuado para obtener la licencia." << std::endl;
    } else {
        std::cout << "Eres un adulto mayor, lo siento, estás sobre la edad establecida." << std::endl;
    }

    return 0;
}




// Practica Tarea #1:

#include <iostream>

int main() {
    std::cout << "Hola Mundo" << std::endl;
    
    return 0;
}



// Practica Tarea #2:

#include <iostream>

int main() {
    int A, B;
    
    std::cout << "Ingrese el primer Valor: ";
    std::cin >> A;

    std::cout << "Ingrese el segundo Valor: ";
    std::cin >> B;

    int suma = A + B;

    std::cout << "La suma de " << A << " + " << B << " = " << suma << std::endl;

    return 0;
}

// Practica Tarea #3:

#include <iostream>

int main() {

    int entero = 100;
    float decimal = 9.99f;
    double doble = 5.6789;
    char caracter = 'Z';
    bool booleano = false;
    
    std::cout << "Entero: " << entero << std::endl;
    std::cout << "Flotante: " << decimal << std::endl;
    std::cout << "Double: " << doble << std::endl;
    std::cout << "Carácter: " << caracter << std::endl;
    std::cout << "Booleano: " << std::boolalpha << booleano << std::endl;

    return 0;
}

//Practica Tarea #4:

#include <iostream>

int main() {
    const double PI = 3.1416;
    double radio;
    
    std::cout << "Ingrese el radio del circulo: ";
    std::cin >> radio;
    
    double area = PI * radio * radio;
    
    std::cout << "Area = " << area << std::endl;
    
    return 0;

}

// Practica Tarea #5:

#include <iostream>

int main() {
    int x;
    int y;
    
    std::cout << "Ingrese valor de X: ";
    std::cin >> x;
    std::cout << "Ingrese valor de Y: ";
    std::cin >> y;

    std::cout << x << " > " << y << " = " << (x > y) << std::endl;
    std::cout << x << " < " << y << " = " << (x < y) << std::endl;
    std::cout << x << " == " << y << " = " << (x == y) << std::endl;
    
    return 0;
}

//Practica Tarea #6:

#include <iostream>

int main() {
    int A;
    std::cout << "Ingresa un numero para saber si es PAR o IMPAR: ";
    std::cin >> A;
    std::cout << A << " es " << (A % 2 == 0 ? "PAR" : "IMPAR") << std::endl;
    return 0;
}

//Practica Tarea #7:

#include <iostream>

int main() {
    int n;
    std::cout << "Ingresa un numero para realizar la tabla: ";
    std::cin >> n;
    for (int i = 1; i <= 10; i++) {
        std::cout << n << " x " << i << " = " << n * i << std::endl;
    }
    return 0;
}

//Practica Tarea #8:





//Practica Tarea Lista de Alumnos:

#include <iostream>
#include <vector>

int main() {
    std::vector<std::string> nombres;

    nombres.push_back("Jose");
    nombres.push_back("Maria");
    nombres.push_back("Juan");

    std::cout << "El vector tiene " << nombres.size() << " elementos." << std::endl;

    std::cout << "El primer elemento es: " << nombres[0] << std::endl;
    std::cout << "El segundo elemento es: " << nombres.at(1) << std::endl;
    std::cout << "El tercer elemento es: " << nombres.at(2) << std::endl;

    std::cout << "Contenido del vector: ";
    for (int i = 0; i < nombres.size(); ++i) {
        std::cout << nombres[i] << " ";
    }
    std::cout << std::endl;

    std::cout << "Contenido con for-each: ";
    for (const auto& nombre : nombres) {
        std::cout << nombre << " ";
    }
    std::cout << std::endl;

    nombres.pop_back(); 
    std::cout << "Después de pop_back(), el último elemento es: " << nombres.back() << std::endl;

    if (!nombres.empty()) {
        std::cout << "El vector no está vacío." << std::endl;
    }

    return 0;
}



// Practica Tarea Carro:

#include <iostream>
#include <string>

class Carro {
public:
    std::string marca;
    std::string modelo;
    int anio;
    int velocidad;

    void acelerar(int aumento) {
        velocidad += aumento;
    }

    void frenar(int decremento) {
        velocidad -= decremento;
    }

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
    mioptra.acelerar(40);
    std::cout << "Velocidad actual: " << mioptra.velocidad << " km/h" << std::endl;
    mioptra.frenar(10);
    std::cout << "Velocidad después de frenar: " << mioptra.velocidad << " km/h" << std::endl;

    return 0;
}


// Practica Tarea Banco:

#include <iostream>
#include <string>

class CuentaBancaria {
private:
    std::string numeroDeCuenta;
    std::string nombreDelTitular;
    double saldo;

public:
    CuentaBancaria(const std::string& numero, const std::string& titular)
        : numeroDeCuenta(numero), nombreDelTitular(titular), saldo(0.0) {}

    void depositar(double cantidad) {
        if (cantidad > 0) {
            saldo += cantidad;
            std::cout << "Depósito exitoso de $" << cantidad << std::endl;
        } else {
            std::cout << "Cantidad inválida para depositar." << std::endl;
        }
    }

    void retirar(double cantidad) {
        if (cantidad <= 0) {
            std::cout << "Cantidad inválida para retirar." << std::endl;
        } else if (cantidad > saldo) {
            std::cout << "Fondos insuficientes para retirar $" << cantidad << std::endl;
        } else {
            saldo -= cantidad;
            std::cout << "Retiro exitoso de $" << cantidad << std::endl;
        }
    }

    double obtenerSaldo() const {
        return saldo;
    }

    void mostrarInformacion() const {
        std::cout << "Número de cuenta: " << numeroDeCuenta << std::endl;
        std::cout << "Titular: " << nombreDelTitular << std::endl;
        std::cout << "Saldo: $" << saldo << std::endl;
    }
};

int main() {
    std::cout << "Estado de Cuenta Bancaria pero no de Venezuela porque es mala" << std::endl;
    CuentaBancaria cuenta("123456789", "Jose Daivid");

    cuenta.mostrarInformacion();
    std::cout << "-----------------------" << std::endl;
    std::cout << "Saldo a depositar" << std::endl;
    cuenta.depositar(500.0);
    std::cout << "-----------------------" << std::endl;
    std::cout << "Saldo a Retirar" << std::endl;
    cuenta.retirar(1000.0);
    std::cout << "-----------------------" << std::endl;
    std::cout << "Ahora si tienes plata, Vamos por el arroz chino" << std::endl;
    cuenta.retirar(200.0);
    std::cout << "-----------------------" << std::endl;
    std::cout << "Estado de Cuenta Bancaria" << std::endl;
    cuenta.mostrarInformacion();

    return 0;
}