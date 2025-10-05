import React from 'react';
import Providers from './providers';

export const metadata = {
  title: 'AI Tools Directory',
  description: 'Catálogo inteligente de herramientas de IA'
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <head />
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}