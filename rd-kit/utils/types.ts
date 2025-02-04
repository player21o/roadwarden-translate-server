type ConverterMap = {
  boolean: (input: string) => boolean;
  number: (input: string) => number;
  string: (input: string) => string;
};

const converterMap: ConverterMap = {
  boolean: (input) => input.toLowerCase() === "true",
  number: (input) => Number(input),
  string: (input) => input,
};

type ParameterConverters<F extends (...args: any[]) => any> = {
  [K in keyof Parameters<F>]: (input: string) => Parameters<F>[K];
};

export function convertArgs<F extends (...args: any[]) => any>(
  fn: F,
  args: string[]
): Parameters<F> {
  // Get the parameter types of the function
  const paramTypes = new Array(args.length).fill("string"); // Simplified assumption
  // In real-world usage, you'd need a runtime type system (like Zod, io-ts, or decorators)

  return args.map((arg, index) => {
    const type = paramTypes[index] as keyof ConverterMap;
    return converterMap[type](arg);
  }) as Parameters<F>;
}
