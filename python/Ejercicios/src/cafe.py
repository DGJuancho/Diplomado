"Ana y Marcos tienen un peculiar horario en sus respectivos trabajos, un día que ambos estén libres quieren tomar un café juntos, pero sucede que Ana está libre cada 2 días y Marcos cada 3. Sabiendo que un día ambos están libres y se tomaron un café, ¿cuántos días debería pasar para que se vuelvan a encontrar y tomar café?"

dias_libres_ana = 2
dias_libres_marcos = 3

dia_actual = 1  # Comenzando a contar el día siguiente al encuentro inicial

while True:
    ana_libre = dia_actual % dias_libres_ana == 0

    marcos_libre = dia_actual % dias_libres_marcos == 0

    # Si ambos están libres en el día actual, hemos encontrado la coincidencia
    if ana_libre and marcos_libre:
        print(
            f"Ana está libre cada {dias_libres_ana} días y Marcos cada  {dias_libres_marcos} días."
        )
        print(
            f"Deberán pasar {dia_actual} días para que se vuelvan a encontrar y tomar café."
        )
        break  # Salimos del bucle una vez que encontramos la coincidencia

    dia_actual += 1  # Pasamos al siguiente día
