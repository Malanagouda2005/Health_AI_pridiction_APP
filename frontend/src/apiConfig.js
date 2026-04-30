export const API_OVERRIDE_STORAGE_KEY = 'HEALTH_AI_BACKEND_URL';

export const isAndroidPlatform = () => {
  if (typeof window === 'undefined') return false;
  const userAgent = navigator?.userAgent?.toLowerCase() || '';
  return /android/i.test(userAgent);
};

export const isCapacitorWebView = () => {
  if (typeof window === 'undefined') return false;
  const protocol = window.location.protocol || '';
  return protocol.startsWith('capacitor') || protocol.startsWith('ionic') || protocol === 'file:';
};

const getApiBaseUrl = () => {
  if (process.env.REACT_APP_API_URL) return process.env.REACT_APP_API_URL;

  const storedOverride = typeof window !== 'undefined' ? localStorage.getItem(API_OVERRIDE_STORAGE_KEY) : null;
  if (storedOverride) return storedOverride;

  if (typeof window === 'undefined') return 'http://localhost:5000';

  const hostname = window.location.hostname;
  const isAndroid = isAndroidPlatform();

  if (hostname === '10.0.2.2') return 'http://10.0.2.2:5000';

  if (isAndroid) {
    // Setting your provided backend IP as the default for Android
    return 'http://10.75.149.30:5000';
  }

  return 'http://localhost:5000';
};

export default getApiBaseUrl;
