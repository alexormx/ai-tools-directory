import React from 'react';
import { ColorModeScript } from '@chakra-ui/react';
import Providers from './providers';
import theme from '../theme';

export const metadata = {
  title: 'AI Tools Directory',
  description: 'Catálogo inteligente de herramientas de IA'
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <head />
      <body>
        <ColorModeScript initialColorMode={theme.config.initialColorMode} />
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}