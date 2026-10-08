import { useState, useCallback } from 'react';
import { Eye, EyeOff, Check, X, AlertCircle, Scale } from 'lucide-react';

/**
 * Validación de entrada — reglas centralizadas.
 * Nota: esta es validación de CLIENTE (UX). El servidor debe replicar
 * estas mismas reglas (p. ej. con class-validator si el backend es NestJS)
 * porque la validación de cliente nunca sustituye la del servidor.
 */
const VALIDATORS = {
  fullName: (value) => {
    const trimmed = value.trim();
    if (!trimmed) return 'El nombre completo es obligatorio';
    if (trimmed.length < 3) return 'Debe tener al menos 3 caracteres';
    if (trimmed.length > 80) return 'No puede exceder 80 caracteres';
    if (!/^[a-zA-ZÀ-ÿñÑ\s'-]+$/.test(trimmed)) return 'Solo se permiten letras y espacios';
    return '';
  },
  email: (value) => {
    const trimmed = value.trim();
    if (!trimmed) return 'El correo electrónico es obligatorio';
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(trimmed)) return 'Ingresa un correo electrónico válido';
    return '';
  },
  phone: (value) => {
    const digits = value.replace(/\D/g, '');
    if (!digits) return 'El teléfono es obligatorio';
    if (digits.length !== 10) return 'Debe tener 10 dígitos';
    return '';
  },
  password: (value) => {
    if (!value) return 'La contraseña es obligatoria';
    if (value.length < 8) return 'Debe tener al menos 8 caracteres';
    if (!/[a-z]/.test(value)) return 'Debe incluir al menos una minúscula';
    if (!/[A-Z]/.test(value)) return 'Debe incluir al menos una mayúscula';
    if (!/[0-9]/.test(value)) return 'Debe incluir al menos un número';
    if (!/[^A-Za-z0-9]/.test(value)) return 'Debe incluir al menos un carácter especial';
    return '';
  },
  confirmPassword: (value, password) => {
    if (!value) return 'Confirma tu contraseña';
    if (value !== password) return 'Las contraseñas no coinciden';
    return '';
  },
};

function passwordStrength(value) {
  let score = 0;
  if (value.length >= 8) score++;
  if (/[a-z]/.test(value) && /[A-Z]/.test(value)) score++;
  if (/[0-9]/.test(value)) score++;
  if (/[^A-Za-z0-9]/.test(value)) score++;
  return score;
}

function formatPhone(digits) {
  const parts = [digits.slice(0, 2), digits.slice(2, 6), digits.slice(6, 10)].filter(Boolean);
  return parts.join(' ');
}

const STRENGTH_LABEL = ['Muy débil', 'Débil', 'Aceptable', 'Fuerte', 'Muy fuerte'];
const STRENGTH_COLOR = ['bg-red-500', 'bg-orange-500', 'bg-amber-500', 'bg-lime-500', 'bg-emerald-500'];

const FIELDS = ['fullName', 'email', 'phone', 'password', 'confirmPassword'];

export default function RegistrationForm() {
  const [values, setValues] = useState({
    fullName: '',
    email: '',
    phone: '',
    userType: 'abogado',
    password: '',
    confirmPassword: '',
  });
  const [errors, setErrors] = useState({});
  const [touched, setTouched] = useState({});
  const [submitted, setSubmitted] = useState(false);
  const [success, setSuccess] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirm, setShowConfirm] = useState(false);

  const runValidation = useCallback((field, value, allValues) => {
    if (field === 'confirmPassword') return VALIDATORS.confirmPassword(value, allValues.password);
    return VALIDATORS[field] ? VALIDATORS[field](value) : '';
  }, []);

  const setFieldValue = (field, rawValue) => {
    const value = field === 'phone' ? formatPhone(rawValue.replace(/\D/g, '').slice(0, 10)) : rawValue;
    const nextValues = { ...values, [field]: value };
    setValues(nextValues);

    if (touched[field] || submitted) {
      setErrors((prev) => ({ ...prev, [field]: runValidation(field, value, nextValues) }));
    }
    if (field === 'password' && (touched.confirmPassword || submitted)) {
      setErrors((prev) => ({
        ...prev,
        confirmPassword: runValidation('confirmPassword', nextValues.confirmPassword, nextValues),
      }));
    }
  };

  const handleBlur = (field) => () => {
    setTouched((prev) => ({ ...prev, [field]: true }));
    setErrors((prev) => ({ ...prev, [field]: runValidation(field, values[field], values) }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const nextErrors = {};
    FIELDS.forEach((f) => {
      nextErrors[f] = runValidation(f, values[f], values);
    });
    setErrors(nextErrors);
    setTouched(FIELDS.reduce((acc, f) => ({ ...acc, [f]: true }), {}));
    setSubmitted(true);

    if (!Object.values(nextErrors).some(Boolean)) {
      setSuccess(true);
    }
  };

  const handleReset = () => {
    setValues({ fullName: '', email: '', phone: '', userType: 'abogado', password: '', confirmPassword: '' });
    setErrors({});
    setTouched({});
    setSubmitted(false);
    setSuccess(false);
  };

  const strength = passwordStrength(values.password);
  // Válido solo si NINGÚN campo obligatorio produce error con los valores actuales.
  // Se recalcula en cada render; es la fuente de verdad para inhabilitar el envío.
  const isFormValid = FIELDS.every((f) => !runValidation(f, values[f], values));

  if (success) {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center p-4">
        <div className="max-w-md w-full bg-white border border-slate-200 shadow-sm rounded-sm p-8 text-center">
          <div className="mx-auto w-12 h-12 rounded-full bg-emerald-50 border border-emerald-200 flex items-center justify-center mb-4">
            <Check className="w-6 h-6 text-emerald-600" />
          </div>
          <h2 className="font-serif text-xl text-slate-900 mb-1">Registro completado</h2>
          <p className="text-sm text-slate-500 mb-6">
            La cuenta de {values.fullName.trim()} fue registrada correctamente.
          </p>
          <button
            type="button"
            onClick={handleReset}
            className="w-full bg-slate-900 hover:bg-slate-800 text-white text-sm font-medium py-2.5 rounded-sm transition-colors"
          >
            Registrar otro usuario
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 flex items-center justify-center p-4">
      <div className="max-w-md w-full bg-white border border-slate-200 shadow-sm rounded-sm overflow-hidden">
        <div className="bg-slate-900 px-6 py-5">
          <div className="flex items-center gap-2 text-amber-500 mb-1">
            <Scale className="w-4 h-4" />
            <span className="text-[11px] uppercase tracking-widest font-medium">Sistema de Gestión Legal</span>
          </div>
          <h1 className="font-serif text-2xl text-white">Registro de usuario</h1>
        </div>
        <div className="h-1 bg-amber-600" />

        <form onSubmit={handleSubmit} noValidate className="p-6 space-y-4">
          {/* Nombre completo */}
          <Field label="Nombre completo" htmlFor="fullName" required error={errors.fullName}>
            <input
              id="fullName"
              type="text"
              autoComplete="name"
              value={values.fullName}
              onChange={(e) => setFieldValue('fullName', e.target.value)}
              onBlur={handleBlur('fullName')}
              aria-required="true"
              aria-invalid={!!errors.fullName}
              aria-describedby={errors.fullName ? 'fullName-error' : undefined}
              className={inputClass(errors.fullName)}
              placeholder="Nombre y apellidos"
            />
          </Field>

          {/* Correo */}
          <Field label="Correo electrónico" htmlFor="email" required error={errors.email}>
            <input
              id="email"
              type="email"
              autoComplete="email"
              value={values.email}
              onChange={(e) => setFieldValue('email', e.target.value)}
              onBlur={handleBlur('email')}
              aria-required="true"
              aria-invalid={!!errors.email}
              aria-describedby={errors.email ? 'email-error' : undefined}
              className={inputClass(errors.email)}
              placeholder="nombre@despacho.com"
            />
          </Field>

          {/* Teléfono */}
          <Field label="Teléfono" htmlFor="phone" required error={errors.phone}>
            <input
              id="phone"
              type="tel"
              inputMode="numeric"
              autoComplete="tel-national"
              value={values.phone}
              onChange={(e) => setFieldValue('phone', e.target.value)}
              onBlur={handleBlur('phone')}
              aria-required="true"
              aria-invalid={!!errors.phone}
              aria-describedby={errors.phone ? 'phone-error' : undefined}
              className={inputClass(errors.phone)}
              placeholder="81 1234 5678"
            />
          </Field>

          {/* Tipo de usuario */}
          <Field label="Tipo de usuario" htmlFor="userType">
            <select
              id="userType"
              value={values.userType}
              onChange={(e) => setFieldValue('userType', e.target.value)}
              className={inputClass(null) + ' bg-white'}
            >
              <option value="abogado">Abogado</option>
              <option value="asistente">Asistente</option>
              <option value="cliente">Cliente</option>
            </select>
          </Field>

          {/* Contraseña */}
          <Field label="Contraseña" htmlFor="password" required error={errors.password}>
            <div className="relative">
              <input
                id="password"
                type={showPassword ? 'text' : 'password'}
                autoComplete="new-password"
                value={values.password}
                onChange={(e) => setFieldValue('password', e.target.value)}
                onBlur={handleBlur('password')}
                aria-required="true"
                aria-invalid={!!errors.password}
                aria-describedby={errors.password ? 'password-error' : 'password-strength'}
                className={inputClass(errors.password) + ' pr-10'}
                placeholder="Mínimo 8 caracteres"
              />
              <button
                type="button"
                onClick={() => setShowPassword((s) => !s)}
                aria-label={showPassword ? 'Ocultar contraseña' : 'Mostrar contraseña'}
                className="absolute right-2.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600"
              >
                {showPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
              </button>
            </div>
            {values.password && (
              <div id="password-strength" className="mt-2">
                <div className="flex gap-1">
                  {[0, 1, 2, 3].map((i) => (
                    <div
                      key={i}
                      className={`h-1 flex-1 rounded-full ${i < strength ? STRENGTH_COLOR[strength] : 'bg-slate-200'}`}
                    />
                  ))}
                </div>
                <p className="text-[11px] text-slate-500 mt-1">{STRENGTH_LABEL[strength]}</p>
              </div>
            )}
          </Field>

          {/* Confirmar contraseña */}
          <Field label="Confirmar contraseña" htmlFor="confirmPassword" required error={errors.confirmPassword}>
            <div className="relative">
              <input
                id="confirmPassword"
                type={showConfirm ? 'text' : 'password'}
                autoComplete="new-password"
                value={values.confirmPassword}
                onChange={(e) => setFieldValue('confirmPassword', e.target.value)}
                onBlur={handleBlur('confirmPassword')}
                aria-required="true"
                aria-invalid={!!errors.confirmPassword}
                aria-describedby={errors.confirmPassword ? 'confirmPassword-error' : undefined}
                className={inputClass(errors.confirmPassword) + ' pr-10'}
                placeholder="Repite la contraseña"
              />
              <button
                type="button"
                onClick={() => setShowConfirm((s) => !s)}
                aria-label={showConfirm ? 'Ocultar contraseña' : 'Mostrar contraseña'}
                className="absolute right-2.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600"
              >
                {showConfirm ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
              </button>
              {values.confirmPassword && !errors.confirmPassword && touched.confirmPassword && (
                <Check className="w-4 h-4 text-emerald-600 absolute right-9 top-1/2 -translate-y-1/2" />
              )}
            </div>
          </Field>

          <button
            type="submit"
            disabled={!isFormValid}
            aria-disabled={!isFormValid}
            className={`w-full text-sm font-medium py-2.5 rounded-sm transition-colors mt-2 ${
              isFormValid
                ? 'bg-slate-900 hover:bg-slate-800 text-white cursor-pointer'
                : 'bg-slate-200 text-slate-400 cursor-not-allowed'
            }`}
          >
            Registrar usuario
          </button>

          {submitted && Object.values(errors).some(Boolean) && (
            <p className="text-xs text-red-600 flex items-center gap-1.5" role="alert">
              <AlertCircle className="w-3.5 h-3.5 flex-shrink-0" />
              Corrige los campos marcados antes de continuar.
            </p>
          )}
        </form>
      </div>
    </div>
  );
}

function inputClass(error) {
  return `w-full border rounded-sm px-3 py-2 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition-colors focus:ring-2 ${
    error
      ? 'border-red-400 focus:ring-red-200 focus:border-red-500'
      : 'border-slate-300 focus:ring-amber-200 focus:border-amber-600'
  }`;
}

function Field({ label, htmlFor, required, error, children }) {
  return (
    <div>
      <label htmlFor={htmlFor} className="block text-xs uppercase tracking-wide font-medium text-slate-500 mb-1.5">
        {label} {required && <span className="text-amber-600">*</span>}
      </label>
      {children}
      {error && (
        <p id={`${htmlFor}-error`} className="text-xs text-red-600 mt-1 flex items-center gap-1" role="alert">
          <AlertCircle className="w-3 h-3 flex-shrink-0" />
          {error}
        </p>
      )}
    </div>
  );
}
