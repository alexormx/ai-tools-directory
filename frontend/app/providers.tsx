"use client";
import { ChakraProvider, extendTheme, ThemeConfig } from '@chakra-ui/react';
import React from 'react';

const config: ThemeConfig = {
  initialColorMode: 'light',
  useSystemColorMode: false
};

const theme = extendTheme({ config });

export default function Providers({ children }: { children: React.ReactNode }) {
  return <ChakraProvider theme={theme}>{children}</ChakraProvider>;
}

export { theme };