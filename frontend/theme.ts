import { extendTheme } from '@chakra-ui/react';

const theme = extendTheme({
  config: { initialColorMode: 'light', useSystemColorMode: false },
  colors: {
    brand: {
      50: '#eef6ff',
      500: '#1976d2',
      600: '#155fae'
    }
  }
});

export default theme;