// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.materialproviderstestvectorkeys.model;

import java.util.Objects;

public class GetKeyDescriptionOutput {
  private final KeyDescription keyDescription;

  protected GetKeyDescriptionOutput(BuilderImpl builder) {
    this.keyDescription = builder.keyDescription();
  }

  public KeyDescription keyDescription() {
    return this.keyDescription;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    Builder keyDescription(KeyDescription keyDescription);

    KeyDescription keyDescription();

    GetKeyDescriptionOutput build();
  }

  static class BuilderImpl implements Builder {
    protected KeyDescription keyDescription;

    protected BuilderImpl() {
    }

    protected BuilderImpl(GetKeyDescriptionOutput model) {
      this.keyDescription = model.keyDescription();
    }

    public Builder keyDescription(KeyDescription keyDescription) {
      this.keyDescription = keyDescription;
      return this;
    }

    public KeyDescription keyDescription() {
      return this.keyDescription;
    }

    public GetKeyDescriptionOutput build() {
      if (Objects.isNull(this.keyDescription()))  {
        throw new IllegalArgumentException("Missing value for required field `keyDescription`");
      }
      return new GetKeyDescriptionOutput(this);
    }
  }
}
