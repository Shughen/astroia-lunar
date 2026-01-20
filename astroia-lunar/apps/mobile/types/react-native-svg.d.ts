/**
 * Déclarations de types temporaires pour react-native-svg
 * À supprimer une fois le package installé (npm install)
 */

declare module 'react-native-svg' {
  import { Component, ReactNode } from 'react';
  import { ViewProps } from 'react-native';

  interface CommonProps {
    fill?: string;
    stroke?: string;
    strokeWidth?: number | string;
    strokeLinecap?: 'butt' | 'round' | 'square';
    strokeLinejoin?: 'miter' | 'round' | 'bevel';
    strokeDasharray?: string | number[];
    opacity?: number;
    transform?: string;
  }

  interface SvgProps extends ViewProps {
    width?: number | string;
    height?: number | string;
    viewBox?: string;
    children?: ReactNode;
  }

  interface CircleProps extends CommonProps {
    cx?: number | string;
    cy?: number | string;
    r?: number | string;
  }

  interface LineProps extends CommonProps {
    x1?: number | string;
    y1?: number | string;
    x2?: number | string;
    y2?: number | string;
  }

  interface TextProps extends CommonProps {
    x?: number | string;
    y?: number | string;
    fontSize?: number | string;
    textAnchor?: 'start' | 'middle' | 'end';
    fontWeight?: string;
    children?: ReactNode;
  }

  interface GProps extends CommonProps {
    children?: ReactNode;
  }

  interface PathProps extends CommonProps {
    d?: string;
  }

  interface RectProps extends CommonProps {
    x?: number | string;
    y?: number | string;
    width?: number | string;
    height?: number | string;
    rx?: number | string;
    ry?: number | string;
  }

  interface DefsProps {
    children?: ReactNode;
  }

  interface ClipPathProps {
    id?: string;
    children?: ReactNode;
  }

  export class Svg extends Component<SvgProps> {}
  export class Circle extends Component<CircleProps> {}
  export class Line extends Component<LineProps> {}
  export class Text extends Component<TextProps> {}
  export class G extends Component<GProps> {}
  export class Path extends Component<PathProps> {}
  export class Rect extends Component<RectProps> {}
  export class Defs extends Component<DefsProps> {}
  export class ClipPath extends Component<ClipPathProps> {}

  export default Svg;
}
