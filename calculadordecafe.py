import streamlit as st

# Título de la aplicación
st.title("Calculadora de Precio Real de Café")

# Selección del tipo de café
tipo_cafe = st.radio("Selecciona el tipo de café:", ("Café Pergamino", "Café Verde"))

# Ingreso del peso del café en gramos
peso_cafe = st.number_input("Ingresa el peso del café en gramos:", min_value=1, value=1000)

# Ingreso del porcentaje de pérdida de peso
porcentaje_perdida = st.number_input("Ingresa el porcentaje de pérdida de peso (%):", min_value=0, max_value=100, value=10)

# Ingreso del precio de tostado por kilo
precio_tostado_por_kilo = st.number_input("Ingresa el precio de tostado por kilo (en tu moneda):", min_value=0.0, value=5.0)

# Ingreso del precio del café
precio_cafe = st.number_input("Ingresa el precio del café (en tu moneda):", min_value=0.0, value=10.0)

# Cálculo del peso real después de la pérdida de peso
peso_real = peso_cafe * (1 - porcentaje_perdida / 100)

# Cálculo del precio de tostado total
precio_tostado_total = (peso_real / 1000) * precio_tostado_por_kilo

# Cálculo del precio total del café (café + tostado)
precio_total = precio_cafe + precio_tostado_total

# Cálculo del precio real por gramo de café después de la pérdida de peso
precio_real_por_gramo = precio_total / peso_real

# Mostrar resultados
st.subheader("Resultados:")
st.write(f"Peso real del café después de la pérdida de peso: {peso_real:.2f} gramos")
st.write(f"Precio total del café (café + tostado): {precio_total:.2f} {st.session_state.get('moneda', 'unidades monetarias')}")
st.write(f"Precio real por gramo de café después de la pérdida de peso: {precio_real_por_gramo:.4f} {st.session_state.get('moneda', 'unidades monetarias')} por gramo")

# Mostrar resultados antes y después del pago del tostado
st.subheader("Comparación antes y después del pago del tostado:")
st.write(f"Precio por gramo antes del tostado: {precio_cafe / peso_cafe:.4f} {st.session_state.get('moneda', 'unidades monetarias')} por gramo")
st.write(f"Precio por gramo después del tostado: {precio_real_por_gramo:.4f} {st.session_state.get('moneda', 'unidades monetarias')} por gramo")
